from django.db import models


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=25)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Source(models.Model):
    name = models.CharField(max_length=64)
    source_url = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, blank=True)
    email = models.EmailField(blank=True)