from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    username = None # this is done to overide the default django settings which require username for login
    
    USERNAME_FIELD = 'email' # overiding username for the email field.
    
    REQUIRED_FIELDS = []
