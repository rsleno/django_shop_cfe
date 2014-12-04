# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20141110_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 17, 54, 16, 248930, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 17, 54, 16, 248990, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
