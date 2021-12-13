from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import user_logged_in, user_logged_out

# import models
from .models import Profile, Notification


# Create a profile instance when a user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Save profile instance whenever a user object is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Create Welcome notifications when a user creates an account
@receiver(post_save, sender=User)
def create_welcome_notifications(sender, **kwargs):
    if kwargs.get('created', False):
        Notification.objects.create(
            user=kwargs.get('instance'),
            title="WELCOME TO X-POS",
            message="We will help you manage your business effectively.")

        Notification.objects.create(
            user=kwargs.get('instance'),
            title="EVERYTHING IN ONE PLACE",
            message="With X-POS, we have automated most of the process so you don't have to repeat yourself. It's that simple.")

        Notification.objects.create(
            user=kwargs.get('instance'),
            title="UPGRADE TO PRO",
            message="Get the more of XPOS with the pro version.")
