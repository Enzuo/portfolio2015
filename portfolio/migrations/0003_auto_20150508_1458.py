# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_tech_icon_g'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_fr', models.CharField(max_length=200, null=True)),
                ('title_zh', models.CharField(max_length=200, null=True)),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_fr', models.TextField(null=True)),
                ('content_zh', models.TextField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='tech',
            old_name='_icon',
            new_name='icon',
        ),
    ]
