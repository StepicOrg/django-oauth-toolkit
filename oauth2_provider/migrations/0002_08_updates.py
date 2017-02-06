# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('oauth2_provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Application',
            name='user',
            field=models.ForeignKey(related_name='oauth2_provider_application', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='AccessToken',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
