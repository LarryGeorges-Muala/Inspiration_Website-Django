# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name_value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Author_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_pic_value', models.CharField(max_length=500)),
                ('author_name_pic_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspiration.Author_Name')),
            ],
        ),
        migrations.CreateModel(
            name='Author_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_text_value', models.CharField(max_length=1000)),
                ('author_name_text_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspiration.Author_Name')),
            ],
        ),
        migrations.CreateModel(
            name='Author_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_url_value', models.CharField(max_length=500)),
                ('author_name_url_reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspiration.Author_Name')),
            ],
        ),
    ]
