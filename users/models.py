from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField

from currency.models import Opportunity


class User(AbstractUser):

    avatar = models.ImageField(
        upload_to='avatars',
        verbose_name=_('Avatar'),
        null=True,
    )
    about = models.TextField(
        verbose_name=_('About'),
    )
    favourite_book = models.CharField(
        max_length=255,
        verbose_name=_('Favourite book'),
        null=True,
    )
    favourite_author = models.CharField(
        max_length=255,
        verbose_name=_('Favourite author'),
        null=True,
    )
    reading_preferences = models.CharField(
        max_length=255,
        verbose_name=_('Reading preferences'),
        null=True,
    )
    phone = PhoneNumberField(
        verbose_name=_('Phone'),
        null=True,
    )
    city = models.CharField(
        max_length=100,
        verbose_name=_('City'),
        null=True,
    )
    novaposhta_number = models.CharField(
        max_length=20,
        verbose_name=_('Novaposhta department number'),
        null=True,
    )

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})

    @property
    def opportunities(self):
        return Opportunity.objects.filter(user=self).count_values()['value__sum']
