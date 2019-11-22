from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()

    #gives nested names to configurations and keeps configurations in the same place 
    class Meta: # specify model we want the form to interact with   
        model = User
        fields = ['username', 'email','password1', 'password2']


#they will LOOK LIKE ONE FORM
#update user name and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    #gives nested names to configurations and keeps configurations in the same place 
    class Meta: # specify model we want the form to interact with   
        model = User
        fields = ['username', 'email']

#update user image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']