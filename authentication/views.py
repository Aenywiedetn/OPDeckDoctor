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
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator

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
       

        email_subject = 'Activate your account on OPDeckDoctor'
        email_body = 'Hi '+ user.username + '! Please verify Your account via this link: \n' + activate_url
        email = EmailMessage(
          email_subject,
          email_body,
          "opdeckdoctorvalidator@gmail.com",
          [email],
        )
        email.send()
        messages.success(request, 'Account successfully created, please check Your email to verify')
        return render(request, 'authentication/register.html')


    return render(request, 'authentication/register.html')
  
class LoginView(View):
  def post(self, request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active == True:
          auth.login(request, user)
          messages.success(request,'Welcome aboard, '+user.username)
          return redirect('decks')
        else:
          messages.error(request, 'Account is not active, please check Your email')
          return redirect('login')
    else:
      messages.error(request, 'Credentials do not match the database, please register or activate account')
      return redirect('login')
  
  def get(self, request):
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
  

class RequestPasswordResetEmail(View):
  def get(self, request):
    return render(request, 'authentication/reset-password.html')
    
  def post(self, request):

    email=request.POST['email']
    context={
      'values':request.POST
    }

    if not validate_email(email):
      messages.error(request, 'Email invalid')
      return render(request, 'authentication/reset-password.html', context)

    user=User.objects.filter(email=email).first()

    if user:
      token_generator = PasswordResetTokenGenerator()
      email_contents = {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        }
      domain = get_current_site(request).domain
      link = reverse('reset-user-password', kwargs={'uidb64': email_contents['uid'], 'token':email_contents['token']})
      reset_url = 'http://'+domain+link

      email_subject = 'Reset Your password on OPDeckDoctor - ' + user.username
      email_body = 'Please use this link to reset Your password: \n' + reset_url
      email = EmailMessage(
        email_subject,
        email_body,
        "opdeckdoctorvalidator@gmail.com",
        [email],
          )
      email.send()     
    messages.success(request, 'Email with password reset link sent')
    return render(request, 'authentication/reset-password.html')
    
  
class CompletePasswordReset(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
        }
        return render(request, 'authentication/set-new-password.html', context)
      
    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
        }

        password = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')

        if not (password and password2):
            messages.error(request, 'Passwords not provided')
            return render(request, 'authentication/set-new-password.html', context)

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'authentication/set-new-password.html', context)
        
        if len(password) < 6:
            messages.error(request, 'Password needs to be at least 6 characters')
            return render(request, 'authentication/set-new-password.html', context)
        
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(User, pk=user_id)
            user.set_password(password)
            user.save(update_fields=["password"])

            messages.success(request, 'Password changed!')
            return redirect('login')
        
        except Exception as e:
            messages.error(request, 'Something went wrong: {}'.format(e))
            return render(request, 'authentication/set-new-password.html', context)
    
    
   