from django.shortcuts import render
from django.http import JsonResponse
from .models import Card

# Create your views here.
def index(request):
  cards = Card.objects.all()
  context = { 'cards' : cards}
  return render(request, 'collector/filters.html', context)

