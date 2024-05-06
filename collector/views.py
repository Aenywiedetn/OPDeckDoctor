from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Card, UserInput
from django.contrib.auth.decorators import login_required
from .forms import UserNumberForm, UserNoteForm
from django.contrib import messages
from .tests import card_order_check
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404




def extra_copies(request, user_id=None):
    User = get_user_model()

    if user_id is not None:
        user = get_object_or_404(User, id=user_id)
        seller_username = user.username
    else:
        user = request.user
        seller_username = user.username

    # Get cards with more than 4 copies for the specified user
    cards_with_extra_copies = Card.objects.filter(userinput__user=user, userinput__number_owned__gt=4)

    # Create a list to store tuples of (card object, extra copies)
    extra_copies_list = []

    for card in cards_with_extra_copies:
        user_input = UserInput.objects.get(user=user, card=card)
        extra_copies = user_input.number_owned - 4

        if extra_copies > 0:
            extra_copies_list.append((card, extra_copies))

    context = {'extra_copies_list': extra_copies_list, 'seller_username': seller_username}
    return render(request, 'collector/extra_copies.html', context)


def index(request):
  cards = Card.objects.all()
  context = { 'cards' : cards }
  return render(request, 'collector/index.html', context)


@login_required(login_url='/authentication/login')
def collector(request):
    cards = Card.objects.all()
    context = {'cards': cards }
    return render(request, 'collector/collector.html', context)


def load_user_inputs(request):
    if request.user.is_authenticated:
        user_inputs = list(UserInput.objects.filter(user=request.user).values())
        return JsonResponse({'user_inputs': user_inputs})
    return JsonResponse({'user_inputs': []})


@login_required(login_url='/authentication/login')
def update_number_owned(request, card_id):
    card = Card.objects.get(idx=card_id)

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
                return JsonResponse({'success': True, 'card_id': card.idx, 'new_number_owned': user_input.number_owned})
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
    card = Card.objects.get(idx=card_id)

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
                return JsonResponse({'success': True, 'card_id': card.idx, 'new_short_note': user_input.short_note})
            else:
                return JsonResponse({'success': False})
        else:
            pass
    else:
        user_input, created = UserInput.objects.get_or_create(card=card, user=request.user, defaults={'short_note': ''})
        form = UserNoteForm(instance=user_input)

    return render(request, 'collector/collector.html', {'form': form, 'card': card})


