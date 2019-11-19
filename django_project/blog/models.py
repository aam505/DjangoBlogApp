from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    #timezone is a function but we do not put () as we do not want to execute it at that point 
    date_posted = models.DateTimeField(default = timezone.now) # auto_now_add=True set only when object is created - with argument you can never update the value of the date posted
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user created post and user deleted do we want to delete the post or set the author to none? in this case we delete ost

    def __str__(self):
        return self.title;
    