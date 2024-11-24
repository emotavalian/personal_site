# Generated by Django 4.2.2 on 2024-11-19 10:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_customuser_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator]),
        ),
    ]
