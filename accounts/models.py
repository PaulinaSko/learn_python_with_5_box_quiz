from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomerUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    login = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
