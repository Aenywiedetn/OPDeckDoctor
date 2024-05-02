from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Card(models.Model):
  lp = models.CharField(default='', primary_key=True)
  idx = models.CharField(default='', unique=True)
  name = models.CharField(default='')
  type = models.CharField(default='')
  set = models.CharField(default='')
  cost = models.CharField(default='')
  color = models.CharField(default='')
  counter = models.BooleanField(default=False)
  counter2k = models.BooleanField(default=False)
  blocker = models.BooleanField(default=False)
  trigger = models.BooleanField(default=False)
  rarity = models.CharField(default='')

class UserInput(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, to_field='idx')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    number_owned = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(2137)])
    short_note = models.CharField(blank=True, null=True, max_length = 30)