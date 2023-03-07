# Generated by Django 4.1.6 on 2023-03-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Euro'), (2, 'US Dollar')], default=2),
        ),
    ]
