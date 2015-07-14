# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room', models.CharField(max_length=100, choices=[(b'Hall', b'Hall'), (b'Kitchen', b'Kitchen'), (b'Lounge', b'Lounge'), (b'Office One', b'Office One')])),
                ('approved', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=False)),
                ('block_booking', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
