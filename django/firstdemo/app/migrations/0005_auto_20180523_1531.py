# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180523_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionlog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
