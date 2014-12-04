# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
