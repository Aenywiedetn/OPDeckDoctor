from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPreference(models.Model):
  user = models.OneToOneField(to=User, on_delete=models.CASCADE)
  leader1 = models.CharField(default='')
  leader2 = models.CharField(default='')
  leader3 = models.CharField(default='')
  