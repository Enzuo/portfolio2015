# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_tag_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='thumb',
            field=models.ImageField(upload_to=b'images/thumb/', blank=True),
        ),
    ]
