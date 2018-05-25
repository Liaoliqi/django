# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180523_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actionlog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=20)),
                ('dist', models.CharField(max_length=255, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updata_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'action_log',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='sex',
            field=models.IntegerField(default=18),
        ),
    ]
