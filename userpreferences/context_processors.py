from userpreferences.models import UserPreference
from django.shortcuts import render, redirect

def user_preferences(request):
    # Check if the user is authenticated before accessing preferences
    if request.user.is_authenticated:
        try:
            user_preferences = UserPreference.objects.get(user=request.user)
        except UserPreference.DoesNotExist:
            user_preferences = None
    else:
        user_preferences = None

    return {'user_preferences': user_preferences}
# myapp/context_processors/user_context.py

def user_username(request):
    # Ensure that the user is authenticated before trying to access the username
    if request.user.is_authenticated:
        return {'user_username': request.user.username}
    else:
        return {}