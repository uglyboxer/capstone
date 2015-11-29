# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('values_array', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.FloatField(default=0))),
                ('guess', models.IntegerField(default=None)),
            ],
        ),
    ]
