# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20150508_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='level',
            field=models.IntegerField(default=50),
        ),
    ]
