from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator

class EmailValidationView(View):
  def post(self, request):
    data=json.loads(request.body)
    email=data['email']
    if not validate_email(email):
      return JsonResponse({'email_error':'( E-mail adress is not valid '}, status=401)
    if User.objects.filter(email=email).exists():
      return JsonResponse({'email_error':'Sorry, this email is already in use'}, status=410)
    return JsonResponse({'email_valid':True})

class UsernameValidationView(View):
  def post(self, request):
    data=json.loads(request.body)
    username=data['username']
    if not str(username).isalnum():
      return JsonResponse({'username_error':'( Username should only contain alphanumeric characters! '}, status=400)
    if len(username)>16:
      return JsonResponse({'username_error':'( Username cannot exceed 16 characters! '}, status=400)
    if User.objects.filter(username=username).exists():
      return JsonResponse({'username_error':'Sorry, this username is taken'}, status=409)
    return JsonResponse({'username_valid':True})
  

class PasswordValidationView(View):
  def post(self, request):
    data=json.loads(request.body)
    password=data['password']
    if len(password)<6:
      return JsonResponse({'password_error':'( Password should contain at least 6 characters! '}, status=400)
    return JsonResponse({'password_valid':True})
  
  

class RegistrationView(View):
  def get(self, request):
    return render(request, 'authentication/register.html')
  
  def post(self, request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    context = {
      'fieldValues': request.POST
    }

    if not User.objects.filter(username=username).exists():
      if not User.objects.filter(email=email).exists():
        if len(password)<6:
          return render(request, 'authentication/register.html', context)
        user = User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.is_active = False
        user.save()

        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(request).domain
        link = reverse('activate', kwargs={'uidb64':uidb64, 'token':token_generator.make_token(user)})
        activate_url = 'http://'+domain+link
       

        email_subject = 'Activate your accont on OPDeckDoctor'
        email_body = 'Hi '+ user.username + '! Please verify Your account via this link: \n' + activate_url
        email = EmailMessage(
          email_subject,
          email_body,
          "noreply@semycolon.com",
          [email],
        )
        email.send()
        messages.success(request, 'Account successfully created')
        return render(request, 'authentication/register.html')


    return render(request, 'authentication/register.html')
  
class LoginView(View):
  def get(self, request):
    return render(request, 'authentication/login.html')
    
  def post(self, request):
    username = request.POST['username']
    password = request.POST['password']

    if username and password:
      user=auth.authenticate(username=username, password=password)

      if user:
        if user.is_active:
          auth.login(request, user)
          messages.success(request,'Welcome aboard, '+user.username)
          return redirect('decks')

        messages.error(request, 'Account is not active, please contact our support')
      messages.error(request, 'Credentials do not match the database, please register or try again')
    messages.error(request, 'Please fill all fields')
    return render(request, 'authentication/login.html')
  
class LogoutView(View):
  def post(self, request):
    auth.logout(request)
    messages.success(request, 'You logged out!')
    return redirect('login')

class VerificationView(View):
  def get(self, request, uidb64, token ):
      id = force_str(urlsafe_base64_decode(uidb64))
      user = User.objects.get(pk=id)

      if user.is_active:
        return redirect('login')
      
      user.is_active=True
      user.save()

      messages.success(request, 'Account activated successfully!')
      return redirect('login')
  

  