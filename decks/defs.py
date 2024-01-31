from django.shortcuts import render
from .models import Card, Deck
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from OPDeckDoctor2.rounding import round_up
from collections import Counter


def deckView(leader_number, leader_set):
  deck_instances = Deck.objects.filter(leader=leader_number, set=leader_set)
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

  card_counts = Counter(giga)

  avg = [
    [
        round_up((count / deck_counter), 2) if deck_counter > 0 else 0,  # Average count from all decklists (position 0)
        card,  # Card name (position 1)
        sum(1 for decklist in decklist_data if card in decklist['decklist'] and giga.count(card) > 0),  # Number of decklists with more than 0 copies (position 2)
        min(decklist['decklist'].count(card) for decklist in decklist_data if card in decklist['decklist']),  # Minimum count of the card in a decklist (position 3)
        max(decklist['decklist'].count(card) for decklist in decklist_data if card in decklist['decklist']),  # Maximum count of the card in a decklist (position 4)
        round_up(sum(decklist['decklist'].count(card) for decklist in decklist_data if card in decklist['decklist']) / sum(1 for decklist in decklist_data if card in decklist['decklist']), 1),  # Average count of the card in one decklist (position 5)
    ]
    for card, count in card_counts.items()
]
  sorted_avg = sorted(avg, key=lambda x: x[0], reverse=True)



  context = {'decklist_data': decklist_data, 'sorted_avg' : sorted_avg, 'deck_counter':deck_counter, 'deck_info':deck_info}

  return context