# Generated by Django 4.2.2 on 2024-11-17 21:13

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=14, region=None, unique=True),
        ),
    ]
