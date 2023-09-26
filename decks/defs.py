from django.shortcuts import render
from .models import Card, Deck
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from OPDeckDoctor2.rounding import round_up


def deckView(leader_number,):
  deck_instances = Deck.objects.filter(leader=leader_number)
  decklist_data = []
  deck_info = Deck.objects.filter(leader=leader_number).first()
  giga = []
  deck_counter = 0
  for i, deck_instance in enumerate(deck_instances, start=1):
        decklist = deck_instance.decklist
        format = deck_instance.format
        decklist_data.append({'index': i, 'decklist': decklist, 'format':format})
  
  for deck_instance in deck_instances:
    giga.extend(deck_instance.decklist)
    deck_counter += 1

  avg = [[round_up((giga.count(card)/deck_counter),2), card] for card in set(giga)]
  sorted_avg = sorted(avg, key=lambda x: x[0], reverse=True)
  context = {'decklist_data': decklist_data, 'sorted_avg' : sorted_avg, 'deck_counter':deck_counter, 'deck_info':deck_info}

  return context