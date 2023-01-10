from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    dob = models.DateField()

