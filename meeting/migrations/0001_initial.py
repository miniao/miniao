# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meetarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('source', models.CharField(max_length=256, verbose_name='\u6765\u6e90')),
                ('author', models.CharField(max_length=256, verbose_name='\u4f5c\u8005')),
                ('browser', models.IntegerField(verbose_name='\u6d4f\u89c8\u91cf')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u4f1a\u8bae',
                'verbose_name_plural': '\u4f1a\u8bae',
            },
        ),
        migrations.CreateModel(
            name='Meetname',
            fields=[
                ('name', models.CharField(max_length=256, serialize=False, verbose_name='\u680f\u76ee\u540d\u79f0', primary_key=True, db_index=True)),
                ('slug', models.CharField(max_length=256, verbose_name='\u680f\u76ee\u7f51\u5740')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u4f1a\u8bae\u680f\u76ee',
                'verbose_name_plural': '\u4f1a\u8bae\u680f\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Meetspecial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u4e13\u9898\u6807\u9898', db_index=True)),
                ('slug', models.CharField(max_length=256, verbose_name='\u4e13\u9898\u7f51\u5740')),
                ('meetimage', models.ImageField(default='defaultuser1.png', upload_to='media/uploads/images/meetspecial/')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u4f1a\u8bae\u4e13\u9898',
                'verbose_name_plural': '\u4f1a\u8bae\u4e13\u9898',
            },
        ),
        migrations.AddField(
            model_name='meetarticle',
            name='column',
            field=models.ForeignKey(verbose_name='\u5f52\u5c5e\u680f\u76ee', to='meeting.Meetname'),
        ),
    ]
