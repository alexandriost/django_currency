from django.db import models
from django.templatetags.static import static
from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    # source = models.CharField(max_length=25)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        ordering = ('-created', )

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


def source_logo_path(instance, filename):
    return f'source_logos/{instance.id}/{filename}'


class Source(models.Model):
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=6, unique=True)
    source_url = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, blank=True)
    email = models.EmailField(blank=True)
    source_logo = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=source_logo_path
    )
    code_name = models.CharField(max_length=64, unique=True)

    @property
    def logo_url(self):
        if self.source_logo:
            return self.source_logo.url

        return static('logo-blank.jpeg')

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request = models.CharField(max_length=255)
    time = models.IntegerField()
