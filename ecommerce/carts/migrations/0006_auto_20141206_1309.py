# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20141122_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 6, 12, 9, 5, 601299, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 6, 12, 9, 5, 601330, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
