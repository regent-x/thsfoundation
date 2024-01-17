# Generated by Django 5.0.1 on 2024-01-17 08:45

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_investor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='Phone_Number',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='Whatsapp_Number',
        ),
        migrations.AddField(
            model_name='investor',
            name='PhoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(default='08023456789', max_length=128, region='NG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investor',
            name='WhatsappNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(default='08023456789', max_length=128, region='NG'),
            preserve_default=False,
        ),
    ]