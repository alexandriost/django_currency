from django.shortcuts import render
from currency.models import Rate, ContactUs


def list_rates(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'list_rates.html', context)


def list_contactus(request):
    contacts = ContactUs.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'list_contactus.html', context)
