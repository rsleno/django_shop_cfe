# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20141110_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='products',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 18, 6, 13, 29659, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 18, 6, 13, 29690, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
