# Generated by Django 5.0.1 on 2024-01-19 23:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_phonenumber_investor_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='Date_of_Birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
