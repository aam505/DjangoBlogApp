from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# This is where you add the logic to how to handle certain routes 
 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

 
def about(request):
    return render(request,'blog/about.html',{'title':'DJANGO'})