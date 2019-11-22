from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom, ProfileUpdateForm, UserUpdateForm
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

    if (request.method == 'POST'):
        #populate with current info of logged in user
        u_form =  UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if(u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()
            messages.success(request,f'User profile updated.')
            return redirect('profile')
            #post redirect pattern? your browser is telling you that you are trying to make another post requist and redirect prevents that
    else:    
        u_form =  UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }   

    return render(request,'users/profile.html', context)