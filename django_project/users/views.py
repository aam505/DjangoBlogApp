from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):

    if (request.method == 'POST'):
        form = UserRegisterFrom(request.POST)
        if (form.is_valid()):
            form.save()  # hashes pwd in bg
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account  created for  {username}. You are able to log in.')
            return redirect('login')
    else:
        form = UserRegisterFrom()

    return render(request,'users/register.html' , {'form':form} ) # form is context to that template so we can accest the form from within the template 

@login_required    
def profile(request):
    return render(request,'users/profile.html')