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
                ('icon', models.ImageField(upload_to=b'')),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('tags', models.ManyToManyField(to='portfolio.Tag')),
                ('techs', models.ManyToManyField(to='portfolio.Tech')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='portfolio.Work', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'portfolio_work_translation',
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='worktranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
