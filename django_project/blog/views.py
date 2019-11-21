from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

# This is where you add the logic to how to handle certain routes 
 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

@login_required     
def about(request):
    return render(request,'blog/about.html',{'title':'DJANGO'})