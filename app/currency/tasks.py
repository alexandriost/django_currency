from celery import shared_task
from django.conf import settings
from currency.choices import RateCurrencyChoices
import requests

@shared_task
def parse_privatbank():
    from currency.models import Rate

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue

        buy = rate['buy']
        sell = rate['sale']
        currency = rate['ccy']

        Rate.objects.create(
            buy=buy,
            sell=sell,
            currency=available_currency[currency]
        )


@shared_task(autoretry_for=(ConnectionError,),
             retry_kwargs={'max_retries': 5})
def send_mail(subject, message):
    raise ConnectionError
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )