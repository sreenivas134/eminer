# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eminer', '0004_newentry_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='newentry',
            name='tags',
        ),
        migrations.AddField(
            model_name='newentry',
            name='tag',
            field=models.ManyToManyField(to='eminer.Tag'),
            preserve_default=True,
        ),
    ]
