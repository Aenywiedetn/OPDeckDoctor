from django.shortcuts import render
from .models import Card, Deck, Leader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from OPDeckDoctor2.rounding import round_up
from .defs import deckView


def landing(request):
  return render(request, 'decks/landing.html')

def index(request):
  return render(request, 'decks/index.html')

def all_leaders(request):
  leaders = Leader.objects.all()
  context = { 'leaders' : leaders}
  return render(request, 'decks/all_leaders.html', context)

def decklistOP04(request, leader):
    deck = deckView(leader)
    context = {'deck': deck , 'leader': leader}
    return render(request, 'decks/leader_view_base.html', context)


