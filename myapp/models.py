from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models



class Image(models.Model):
    # title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    
    title = models.CharField(
        max_length=100,
        
    )
    description = models.CharField(
        max_length=200,
        
    )
    date = models.DateField(
        
    )

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField("Email address", unique=True)
    age = models.IntegerField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []     
    
    
