from .models import FlashCards
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


class FlashCardsForm(forms.ModelForm):
    
    class Meta:
        model = FlashCards
        fields = ['title','description','subject']
        
        
        