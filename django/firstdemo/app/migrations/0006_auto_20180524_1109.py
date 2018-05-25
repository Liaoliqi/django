# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180523_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='today',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.CharField(max_length=20)),
                ('json', models.TextField()),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'today',
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
