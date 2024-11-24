# Generated by Django 4.2.2 on 2024-11-19 11:52

import django.core.validators
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=18, region=None, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\+|09|9)[0-9]{18,}$')]),
        ),
    ]