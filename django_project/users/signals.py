from django.db.models.signals import post_save # signal that gets fired after something gets created
from django.contrib.auth.models import User
#import receiver of the signal
from django.dispatch import receiver
from .models import Profile

# we want a user profile to be created for each new user 

#when a user is saved then send this signal, and the signal will be received by this function create_profile
@receiver(post_save, sender = User)
def create_profile(sender, instance,  created, **kwargs):
    if(created):
        Profile.objects.create(user=instance)


@receiver(post_save, sender = User)
def save_profile(sender, instance,  **kwargs): # excepts any additional arguments 
    instance.profile.save()