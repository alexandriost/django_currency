from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter
from currency.models import Rate, ContactUs, Source


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sale',
        'currency',
        'source',
        'created',
    )
    list_filter = (
        'currency',
        ('created', DateRangeFilter)
    )
    search_fields = (
        'source',
        'buy',
        'sale',
    )


@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'subject',
        'message',
    )

    search_fields = (
        'name',
        'email',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'source_url',
        'phone',
        'email',
    )
    search_fields = (
        'name',
        'source_url',
        'phone',
        'email',
    )
