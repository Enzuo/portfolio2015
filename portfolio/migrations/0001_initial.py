# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('_icon', models.ImageField(upload_to=b'images/icons/', db_column=b'icon')),
                #('icon_g', models.ImageField(upload_to=b'images/icons/')),
                ('notes', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
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
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to=b'images/thumb/', blank=True)),
                ('tags', models.ManyToManyField(to='portfolio.Tag', blank=True)),
                ('techs', models.ManyToManyField(to='portfolio.Tech', blank=True)),
            ],
        ),
    ]
