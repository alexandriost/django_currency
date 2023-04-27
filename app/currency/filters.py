import django_filters
from currency.models import Rate, ContactUs, Source


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sale': ('gt', 'gte', 'lt', 'lte', 'exact'),
        }


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {
            'email': ('icontains',),
            'subject': ('icontains',)
        }


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = ['name', 'code_name', 'phone', 'email']
