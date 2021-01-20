from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField(default=date.today)
    gender = models.CharField(max_length=1)






    
