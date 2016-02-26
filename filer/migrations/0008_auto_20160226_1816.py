# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20160226_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(related_name='owned_files', verbose_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
