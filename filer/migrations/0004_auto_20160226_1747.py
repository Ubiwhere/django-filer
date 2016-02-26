# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0003_auto_20160226_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipboard',
            name='user',
            field=models.ForeignKey(related_name='filer_clipboards', verbose_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
