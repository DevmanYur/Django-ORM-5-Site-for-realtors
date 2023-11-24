# Generated by Django 3.2.21 on 2023-11-24 12:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_rename_owner_pure_phone_flat_one_pure_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='one_pure_phone',
        ),
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]