# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_work_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name_zh',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tech',
            name='group',
            field=models.IntegerField(default=0, help_text=b'0 hidden #1 Framework : Django, # 2 Language : Python, # 3 Special skill : Drawing'),
        ),
    ]
