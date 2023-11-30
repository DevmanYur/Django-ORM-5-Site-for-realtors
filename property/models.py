from django.db import models
from django.forms import Select
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    new_building = models.BooleanField(null=True)

    owner_pure_phone = PhoneNumberField(verbose_name="Нормализованный номер владельца", blank=True)

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    liked_by = models.ManyToManyField(User, related_name="liked_posts")

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Claim(models.Model):
    author = models.ForeignKey(User, verbose_name='Кто жаловался',
                               on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, verbose_name='Квартира, на которую пожаловались', on_delete=models.CASCADE)
    description = models.TextField('Текст жалобы', max_length=5000, blank=True)


class Owner(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_pure_phone = PhoneNumberField(verbose_name="Нормализованный номер владельца", blank=True)
    owner_flat = models.ManyToManyField(Flat,verbose_name="Квартиры в собственности", related_name="owners")


# Owner
# ФИО владельца
# Номер владельца
# Нормальзовыанный номер владельца
# Квартиры в собственности