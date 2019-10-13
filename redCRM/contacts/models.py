from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    SOURCE_TYPES = (
        ('Realtor', 'Realtor'),
        ('FA', 'FA'),
        ('Builder', 'Builder'),
        ('Other', 'Other'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneField(blank=True, unique=True)
    alt_phone = PhoneField(blank=True, unique=True)
    company = models.CharField(max_length=100)
    source_type = models.CharField(max_length=10, choices=SOURCE_TYPES)
    message = models.CharField(max_length=500, blank=True)
    added = models.DateTimeField(auto_now_add=True)
