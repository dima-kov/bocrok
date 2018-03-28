import base64

from django.db import models
from django.core.signing import TimestampSigner
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

from currency.models import Opportunity
from book.models import BookReading


DEFAULT_USER_AVATAR = 'default-avatar.png'


class User(AbstractUser):

    avatar = models.ImageField(
        upload_to='avatars',
        verbose_name=_('Avatar'),
        default=DEFAULT_USER_AVATAR,
        null=True,
    )
    about = models.TextField(
        verbose_name=_('About'),
        null=True,
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
    invited_by = models.ForeignKey(
        "users.Invite",
        related_name='invited_users',
        verbose_name='Invited by invite',
        null=True,
    )

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'pk': self.pk})

    @property
    def opportunities(self):
        return Opportunity.objects.filter(user=self).count_values()

    def get_token(self):
        return TimestampSigner().sign(self.email).split(':', 1)[1]

    def has_enough_to_read(self):
        """
            Returns whether user has enough opportunities to read book
        """
        return self.opportunities >= 1

    def has_unfinished_readings(self):
        return self.book_readings.exclude(status=BookReading.READ).exists()

    def generate_signature(self):
        # only start
        token = TimestampSigner().sign(self.email)
        return base64.urlsafe_b64encode(bytes(token, 'utf8'))

    def get_or_create_invite(self):
        if not hasattr(self, 'invite'):
            inv = Invite.objects.create(
                user=self,
                token=generate_unique_token()
            )
        else:
            inv = self.invite
        return inv.token


class Invite(models.Model):

    user = models.OneToOneField(
        User,
        verbose_name='User',
        related_name='invite'
    )
    token = models.CharField(
        max_length=100,
        verbose_name='Token',
        unique=True,
    )

    class Meta:
        verbose_name = "Invite"
        verbose_name_plural = "Invites"

    def __str__(self):
        return '{} {}'.format(self.user.username, self.token)

    def is_valid(self):
        return self.invited_users.count() < settings.USERS_NUM_TO_INVITE


def generate_unique_token():
    token = get_random_string(length=10)
    if Invite.objects.filter(token=token):
        return generate_unique_token()
    return token
