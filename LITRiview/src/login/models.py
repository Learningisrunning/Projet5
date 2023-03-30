from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    follows = models.ManyToManyField('self',  symmetrical= False, related_name="follows_list")
    followers = models.ManyToManyField('self',  symmetrical= False, related_name="followers_list")
