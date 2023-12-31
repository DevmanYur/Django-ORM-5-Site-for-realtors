# Generated by Django 3.2.21 on 2023-11-30 13:55

from django.db import migrations


def load_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    Flats = Flat.objects.all()
    for Select_flat in Flats:
        Owner.objects.get_or_create(owner_flat = Select_flat.owner_flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20231130_1521'),
    ]

    operations = [migrations.RunPython(load_flats),
    ]
