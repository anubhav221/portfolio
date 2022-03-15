from unittest.util import _MAX_LENGTH
from django.db import models
#from numpy import mafromtxt

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name