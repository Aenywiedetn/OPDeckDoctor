from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Card(models.Model): #archaic model - not deleted because of database migration issues
  id = models.CharField(default='', primary_key=True)
  name = models.CharField(default='')
  type = models.CharField(default='')
  set = models.CharField(default='')
  cost = models.IntegerField(default='')
  color = models.CharField(default='')
  counter = models.IntegerField(default='')
  blocker = models.BooleanField(default=False)
  trigger = models.BooleanField(default=False)

class Deck(models.Model):
  id = models.CharField(default='decklistaDodatek_numer', primary_key=True)
  leader = models.CharField(default='lider')
  name = models.CharField(default='Donquixote Doflamingo')
  color1 = models.CharField(default='Pure')
  color2 = models.CharField(default='Pure')
  set = models.CharField(default='OP00')
  format = models.CharField(default='XXX')
  decklist = ArrayField(models.CharField(), size=50, default=list)

class Leader(models.Model):
  lp = models.CharField(default='', primary_key=True)
  id = models.CharField(default='')
  name = models.CharField(default='')
  set = models.CharField(default='')
  life = models.IntegerField(default='')
  color1 = models.CharField(default='Pure')
  color2 = models.CharField(default='')
  url = models.CharField(default='')