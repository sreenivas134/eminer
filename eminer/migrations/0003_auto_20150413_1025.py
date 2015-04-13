# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('eminer', '0002_auto_20150413_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newentry',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
