# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tech',
            name='icon_g',
            field=models.ImageField(upload_to=b'images/icons/', blank=True),
        ),
    ]
