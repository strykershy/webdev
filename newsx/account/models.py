from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    dob = models.DateField(null=True, blank=True)

