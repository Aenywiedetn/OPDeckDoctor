from django.shortcuts import render
from .models import Card, Deck, Leader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from OPDeckDoctor2.rounding import round_up
from .defs import deckView
#from .models import Card
# Create your views here.

#@login_required(login_url='/authentication/login')
def index(request):
  return render(request, 'decks/index.html')

def all_leaders(request):
  leaders = Leader.objects.all()
  context = { 'leaders' : leaders}
  return render(request, 'decks/all_leaders.html', context)

def decklistOP04(request, leader):
  context = deckView(leader)
  return render(request, 'decks/leader_view_base.html', context)


