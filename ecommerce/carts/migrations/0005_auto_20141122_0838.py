# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20141110_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, to='carts.Cart', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_total',
            field=models.DecimalField(default=10.99, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 22, 7, 38, 18, 219883, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 22, 7, 38, 18, 219923, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
