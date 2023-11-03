# myapp/middleware.py

from userpreferences.models import UserPreference  # Import your UserPreferences model

class UserPreferencesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            try:
                # Try to fetch the user's preferences
                user_preferences = UserPreference.objects.get(user=request.user)
            except UserPreference.DoesNotExist:
                # Handle the case where preferences don't exist, e.g., set a default value
                user_preferences = None  # or set some default values

            # Add user_preferences to the request object so it's available in views
            request.user_preferences = user_preferences

        response = self.get_response(request)
        return response