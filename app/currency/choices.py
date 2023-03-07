from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'Euro'
    USD = 2, 'US Dollar'
