from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# This is where you add the logic to how to handle certain routes 
 
def home(request):
    return HttpResponse('<h1>Blog home</h1>')


def about(request):
    return HttpResponse('<h1>Blog about</h1>')