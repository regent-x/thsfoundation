# Generated by Django 5.0.1 on 2024-01-18 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_investor_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor',
            old_name='PhoneNumber',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='investor',
            old_name='Ref_id',
            new_name='Ref',
        ),
        migrations.RenameField(
            model_name='investor',
            old_name='WhatsappNumber',
            new_name='Whatsapp',
        ),
    ]
