import django_filters

from currency.models import Rate, Source


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = ['buy', 'sale']


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = ['name', 'code_name', 'phone', 'email']
