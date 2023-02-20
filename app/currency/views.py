from django.shortcuts import render
from django.http import HttpResponse
from currency.models import Rate, ContactUs


def list_rates(request):
    qs = Rate.objects.all()
    result = []

    for rate in qs:
        result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell},currency: {rate.currency},source: {rate.source}, created: {rate.created} <br>')

    return HttpResponse(str(result))


def list_contactus(request):
    qs = ContactUs.objects.all()
    result = []

    for message in qs:
        result.append(f'id: {message.id}, email_from: {message.email_from}, subject: {message.subject}, message: {message.message}')

    return HttpResponse(str(result))