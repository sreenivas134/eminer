# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eminer', '0006_auto_20150413_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newentry',
            name='tag',
            field=models.ManyToManyField(to=b'eminer.Tag', null=True),
        ),
    ]
