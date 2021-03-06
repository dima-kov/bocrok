# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:35
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('author', models.CharField(max_length=250, verbose_name='Author')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='books_image', verbose_name='Image')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
