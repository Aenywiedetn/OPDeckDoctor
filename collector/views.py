from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Card, UserInput
from django.contrib.auth.decorators import login_required
from .forms import UserNumberForm, UserNoteForm
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
def update_number_owned(request, card_id):
    card = Card.objects.get(id=card_id)

    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = UserNumberForm(request.POST)
            if not form.is_valid():
                print(form.errors)
            if form.is_valid():
                number_owned = form.cleaned_data['number_owned']
                user_input, created = UserInput.objects.get_or_create(card=card, user=request.user, defaults={'number_owned': number_owned})
                if not created:
                    user_input.number_owned = number_owned
                    user_input.save()
                return JsonResponse({'success': True, 'card_id': card.id, 'new_number_owned': user_input.number_owned})
            else:
                return JsonResponse({'success': False})
        else:
            pass
    else:
        user_input, created = UserInput.objects.get_or_create(card=card, user=request.user, defaults={'number_owned': 0})
        form = UserNumberForm(instance=user_input)

    return render(request, 'collector/collector.html', {'form': form, 'card': card})

@login_required(login_url='/authentication/login')
def update_short_note(request, card_id):
    card = Card.objects.get(id=card_id)

    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = UserNoteForm(request.POST)
            if not form.is_valid():
                print(form.errors)
            if form.is_valid():
                short_note = form.cleaned_data['short_note']
                user_input, created = UserInput.objects.get_or_create(card=card, user=request.user, defaults={'short_note': short_note})
                if not created:
                    user_input.short_note = short_note
                    user_input.save()
                return JsonResponse({'success': True, 'card_id': card.id, 'new_short_note': user_input.short_note})
            else:
                return JsonResponse({'success': False})
        else:
            pass
    else:
        user_input, created = UserInput.objects.get_or_create(card=card, user=request.user, defaults={'short_note': ''})
        form = UserNoteForm(instance=user_input)

    return render(request, 'collector/collector.html', {'form': form, 'card': card})


@login_required(login_url='/authentication/login')
def collector(request):
    cards = Card.objects.all()
    user_inputs = UserInput.objects.filter(user=request.user)
    context = {'cards': cards, 'user_inputs': user_inputs}
    return render(request, 'collector/collector.html', context)