# Generated by Django 5.0.1 on 2024-01-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_investor_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='Ref',
            field=models.IntegerField(null=True),
        ),
    ]
