# search/models.py

from djongo import models
from db_connection import collection

class Contact(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    sold_sands = models.CharField(max_length=100)
