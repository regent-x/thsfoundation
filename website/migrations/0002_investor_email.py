# Generated by Django 5.0.1 on 2024-01-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
