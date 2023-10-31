from django.db import models

# Create your models here.
class Card(models.Model):
  id = models.CharField(default='', primary_key=True)
  name = models.CharField(default='')
  type = models.CharField(default='')
  set = models.CharField(default='')
  cost = models.IntegerField(default='')
  color = models.CharField(default='')
  counter = models.IntegerField(default='')
  blocker = models.BooleanField(default=False)
  trigger = models.BooleanField(default=False)