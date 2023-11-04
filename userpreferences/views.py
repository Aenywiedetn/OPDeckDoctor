from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
  leader_data=[]
  file_path = os.path.join(settings.BASE_DIR,'leaders.json')
    
  with open(file_path,'r') as json_file:
    data=json.load(json_file)
    for k, v in data.items():
      leader_data.append({'id': k, 'name': v })
  exists = UserPreference.objects.filter(user=request.user).exists()
  user_preferences = None
  if exists:
    user_preferences = UserPreference.objects.get(user=request.user)
  

  if request.method=='GET':
    

    return render(request, 'preferences/index.html',{'leaders':leader_data,'user_preferences': user_preferences})
  
  else:
    leader1 = request.POST['leader1']
    leader2 = request.POST['leader2']
    leader3 = request.POST['leader3']
    
    if exists:
      user_preferences.leader1 = leader1
      user_preferences.leader2 = leader2
      user_preferences.leader3 = leader3

      user_preferences.save()
    else:
      UserPreference.objects.create(user=request.user, leader1=leader1, leader2=leader2, leader3=leader3)

    messages.success(request,'Changes saved')
    return render(request, 'preferences/index.html',{'leaders':leader_data,'user_preferences': user_preferences})