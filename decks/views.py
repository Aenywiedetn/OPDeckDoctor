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

def zoro_op01(request):
  context = deckView('OP01-001')
  return render(request, 'decks/leader_view_base.html', context)

def law_op01(request):
  context = deckView('OP01-002')
  return render(request, 'decks/leader_view_base.html', context)

def luffy_op01(request):
  context = deckView('OP01-003')
  return render(request, 'decks/leader_view_base.html', context)

def oden_op01(request):
  context = deckView('OP01-031')
  return render(request, 'decks/leader_view_base.html', context)

def doflamingo_op01(request):
  context = deckView('OP01-060')
  return render(request, 'decks/leader_view_base.html', context)

def kaido_op01(request):
  context = deckView('OP01-061')
  return render(request, 'decks/leader_view_base.html', context)

def crocodile_op01(request):
  context = deckView('OP01-062')
  return render(request, 'decks/leader_view_base.html', context)

def king_op01(request):
  context = deckView('OP01-091')
  return render(request, 'decks/leader_view_base.html', context)

def whitebeard_op02(request):
  context = deckView('OP02-001')
  return render(request, 'decks/leader_view_base.html', context)

def garp_op02(request):
  context = deckView('OP02-002')
  return render(request, 'decks/leader_view_base.html', context)

def kinemon_op02(request):
  context = deckView('OP02-025')
  return render(request, 'decks/leader_view_base.html', context)

def sanji_op02(request):
  context = deckView('OP02-026')
  return render(request, 'decks/leader_view_base.html', context)

def ivankov_op02(request):
  context = deckView('OP02-049')
  return render(request, 'decks/leader_view_base.html', context)

def magulon_op02(request):
  context = deckView('OP02-071')
  return render(request, 'decks/leader_view_base.html', context)

def zephyr_op02(request):
  context = deckView('OP02-072')
  return render(request, 'decks/leader_view_base.html', context)

def smoker_op02(request):
  context = deckView('OP02-093')
  return render(request, 'decks/leader_view_base.html', context)

def ace_op03(request):
  context = deckView('OP03-001')
  return render(request, 'decks/leader_view_base.html', context)

def kuro_op03(request):
  context = deckView('OP03-021')
  return render(request, 'decks/leader_view_base.html', context)

def arlong_op03(request):
  context = deckView('OP03-022')
  return render(request, 'decks/leader_view_base.html', context)

def nami_op03(request):
  context = deckView('OP03-040')
  return render(request, 'decks/leader_view_base.html', context)

def rizzburg_op03(request):
  context = deckView('OP03-058')
  return render(request, 'decks/leader_view_base.html', context)

def bobgucci_op03(request):
  context = deckView('OP03-076')
  return render(request, 'decks/leader_view_base.html', context)

def linlin_op03(request):
  context = deckView('OP03-077')
  return render(request, 'decks/leader_view_base.html', context)

def katakuri_op03(request):
  context = deckView('OP03-099')
  return render(request, 'decks/leader_view_base.html', context)

def vivi_op04(request):
  context = deckView('OP04-001')
  return render(request, 'decks/leader_view_base.html', context)

def doflamingo_op04(request):
  context = deckView('OP04-019')
  return render(request, 'decks/leader_view_base.html', context)

def issho_op04(request):
  context = deckView('OP04-020')
  return render(request, 'decks/leader_view_base.html', context)

def rebecca_op04(request):
  context = deckView('OP04-039')
  return render(request, 'decks/leader_view_base.html', context)

def queen_op04(request):
  context = deckView('OP04-040')
  return render(request, 'decks/leader_view_base.html', context)

def crocodile_op04(request):
  context = deckView('OP04-058')
  return render(request, 'decks/leader_view_base.html', context)

def luffy_st01(request):
  context = deckView('ST01-001')
  return render(request, 'decks/leader_view_base.html', context)

def kid_st02(request):
  context = deckView('ST02-001')
  return render(request, 'decks/leader_view_base.html', context)

def crocodile_st03(request):
  context = deckView('ST03-001')
  return render(request, 'decks/leader_view_base.html', context)

def kaido_st04(request):
  context = deckView('ST04-001')
  return render(request, 'decks/leader_view_base.html', context)

def shanks_st05(request):
  context = deckView('ST05-001')
  return render(request, 'decks/leader_view_base.html', context)

def sakazuki_st06(request):
  context = deckView('ST06-001')
  return render(request, 'decks/leader_view_base.html', context)

def linlin_st07(request):
  context = deckView('ST07-001')
  return render(request, 'decks/leader_view_base.html', context)

def luffy_st08(request):
  context = deckView('ST08-001')
  return render(request, 'decks/leader_view_base.html', context)

def yamato_st09(request):
  context = deckView('ST09-001')
  return render(request, 'decks/leader_view_base.html', context)

def uta_p011(request):
  context = deckView('ST09-001')
  return render(request, 'decks/leader_view_base.html', context)
