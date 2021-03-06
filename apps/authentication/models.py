from django.db import models
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True  # default user email to unique
Model = models.Model


# Extending user model with profile
class Profile(Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    gender = models.CharField(default="", max_length=1,
                              choices=GENDER_CHOICES,
                              null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile data"


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#       NOTIFICATIONS MODEL
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Notification(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    viewed_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
