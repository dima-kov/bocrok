# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-27 23:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180318_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True, verbose_name='Token')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invite', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Invite',
                'verbose_name_plural': 'Invites',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='invited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_users', to='users.Invite', verbose_name='Invited by invite'),
        ),
    ]