from rest_framework import serializers

from currency.models import Rate, Source, ContactUs
from currency.tasks import send_mail


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'source',
            'currency',
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
        contact_obj = ContactUs.objects.create(
            email_from=validated_data['email_from'],
            subject=validated_data['subject'],
            message=validated_data['message']
        )

        send_mail(validated_data['subject'], validated_data['message'])

        return contact_obj
