# search/models.py

from django.db import models
from db_connection import collection

class Contact(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    sold_sands = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    # sold_sands = models.CharField(max_length=100)
    last_call = models.DateField(blank=True, null=True)


class Phone(models.Model):
    number = models.CharField(max_length=20, unique=True)


class SMS(models.Model):
    twilio_phone = models.ForeignKey(to=Phone, on_delete=models.CASCADE,
                                     default="")
    number = models.CharField(max_length=20, blank=True, null=True)
    msg = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)


class Call(models.Model):
    twilio_phone = models.ForeignKey(to=Phone, on_delete=models.CASCADE,
                                     default="")
    number = models.CharField(max_length=20,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    time_duration = models.IntegerField(default=0)

    # XXX inbound, number, other fields


class CallLogs(models.Model):
    sid = models.CharField(max_length=34, unique=True, null=True, blank=True)
    date = models.DateTimeField()
    from_number = models.CharField(max_length=20, null=True)
    to_number = models.CharField(max_length=20, null=True)
    recording_url = models.CharField(max_length=500, null=True)
    duration = models.CharField(max_length=10, null=True)
    direction = models.CharField(max_length=30, null=True)

    numbers_pressed = models.CharField(max_length=30, null=True)

