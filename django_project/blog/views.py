from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# This is where you add the logic to how to handle certain routes 
 

posts =[
    {
        'author':'Jane Doe',
        'title':'First blog post',
        'content':'First post content',
        'date_posted':'August 27, 2019'
    },
    {
        'author':'Jane Doe',
        'title':'Second blog post',
        'content':'Second post content',
        'date_posted':'August 28, 2019'
    }
]
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html')