# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0005_auto_20160226_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='owner',
            field=models.ForeignKey(related_name='filer_owned_folders', verbose_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='folderpermission',
            name='user',
            field=models.ForeignKey(related_name='filer_folder_permissions', verbose_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
