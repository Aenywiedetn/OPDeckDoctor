from django import forms
from .models import UserInput

class UserNumberForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['number_owned']
        required = False

class UserNoteForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['short_note']
        required = False