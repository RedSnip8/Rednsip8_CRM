from django.db import models
from phone_field import PhoneField
from contacts.models import Contact


class Lead(models.Model):
    LOAN_TYPES = (
        ('Purchase', 'Purchase'),
        ('Refi', 'Refi'),
        ('HEL', 'HEL'),
        ('HELOC', 'HELOC'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneField(blank=True, unique=True)
    alt_phone = PhoneField(blank=True, unique=True)
    loan_type = models.CharField(max_length=10, choices=LOAN_TYPES)
    source = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=500, blank=True)
    generated = models.DateTimeField(auto_now_add=True)
