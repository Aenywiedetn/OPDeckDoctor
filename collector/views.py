from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Card, UserInput
from django.contrib.auth.decorators import login_required
from .forms import UserInputForm
from django.contrib import messages


# Create your views here.
def index(request):
  cards = Card.objects.all()
  context = { 'cards' : cards}
  return render(request, 'collector/index.html', context)

@login_required(login_url='/authentication/login')
def collector(request):
  cards = Card.objects.all()
  context = { 'cards' : cards}
  return render(request, 'collector/collector.html', context)


@login_required(login_url='/authentication/login')
def update_user_input(request, card_id):
    card = Card.objects.get(id=card_id)

    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = UserInputForm(request.POST)
            if form.is_valid():
                number_owned = form.cleaned_data['number_owned']
                user_input, created = UserInput.objects.get_or_create(card=card, user=request.user, defaults={'number_owned': number_owned})
                if not created:
                    user_input.number_owned = number_owned
                    user_input.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})
        else:
            # Handle non-AJAX request (form submission) here
            # You can keep your existing code for form submissions
            # Make sure to indent the code that should be executed when it's not an AJAX request
            pass
    else:
        user_input, created = UserInput.objects.get_or_create(card=card, user=request.user, defaults={'number_owned': 0})
        form = UserInputForm(instance=user_input)

    return render(request, 'collector/collector.html', {'form': form, 'card': card})

@login_required(login_url='/authentication/login')
def collector(request):
    cards = Card.objects.all()
    user_inputs = UserInput.objects.filter(user=request.user)
    context = {'cards': cards, 'user_inputs': user_inputs}
    return render(request, 'collector/collector.html', context)