# Generated by Django 3.2.21 on 2023-11-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20231130_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_flat',
            field=models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
