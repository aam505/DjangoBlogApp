from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()

    #gives nested names to configurations and keeps configurations in the same place 
    class Meta: # specify model we want the form to interact with   
        model = User
        fields = ['username', 'email','password1', 'password2']