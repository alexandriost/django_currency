from django.db import models
from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    # source = models.CharField(max_length=25)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)

    def __str__(self):
        return f'| Id-{self.id} | Currency: {self.get_currency_display()} | Buy: {self.buy} |'


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'


class Source(models.Model):
    name = models.CharField(max_length=64)
    source_url = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request = models.CharField(max_length=255)
    time = models.IntegerField()
