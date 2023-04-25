from rest_framework import serializers

from currency.models import Rate, Source, ContactUs
from currency.tasks import send_mail
from django.conf import settings


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'source'
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'code_name',
            'source_url',
            'phone',
            'email'
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )

    def create(self, validated_data):
        contactus = ContactUs.objects.create(**validated_data)
        recipient = settings.DEFAULT_FROM_EMAIL
        from django.core.mail import send_mail
        send_mail(
            validated_data['subject'],
            validated_data['message'],
            validated_data['email_from'],
            ['recipient'],
            fail_silently=False,
        )
        return contactus
