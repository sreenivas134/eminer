# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eminer', '0004_newentry_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newentry',
            name='tags',
        ),
    ]
