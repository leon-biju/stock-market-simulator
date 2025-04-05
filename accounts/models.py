from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  #username and password already included
  #user can start with 100k gbp to trade
  starting_balance = models.DecimalField(max_digits=10, decimal_places=2, default=100000.00)
  current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=100000.00)