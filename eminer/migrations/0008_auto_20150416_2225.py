# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eminer', '0007_auto_20150416_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newentry',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newentry',
            name='tag',
            field=models.ManyToManyField(to=b'eminer.Tag'),
        ),
    ]
