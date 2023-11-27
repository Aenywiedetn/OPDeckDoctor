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

def charts(request):
    return render(request, 'decks/charts.html')

def all_leaders(request):
  leaders = Leader.objects.all()
  context = { 'leaders' : leaders}
  return render(request, 'decks/all_leaders.html', context)

def decklist(request, leader, deck_set):
    op01 = Deck.objects.filter(leader=leader, set='OP01').first()
    op02 = Deck.objects.filter(leader=leader, set='OP02').first()
    op03 = Deck.objects.filter(leader=leader, set='OP03').first()
    op04 = Deck.objects.filter(leader=leader, set='OP04').first()
    op05 = Deck.objects.filter(leader=leader, set='OP05').first()
    op06 = Deck.objects.filter(leader=leader, set='OP06').first()
    deck = deckView(leader, deck_set)
    currentFormat = deck_set
    context = {'deck': deck , 'leader': leader, 'op01' : op01, 'op02' : op02, 'op03' : op03, 'op04' : op04, 'op05' : op05, 'op06' : op06,'currentFormat' : currentFormat }
    return render(request, 'decks/leader_view_base.html', context)


