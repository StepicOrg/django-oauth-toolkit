# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import oauth2_provider.validators
import oauth2_provider.generators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('token', models.CharField(db_index=True, max_length=255)),
                ('expires', models.DateTimeField()),
                ('scope', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('client_id', models.CharField(max_length=100, unique=True, default=oauth2_provider.generators.generate_client_id, db_index=True)),
                ('redirect_uris', models.TextField(help_text='Allowed URIs list, space separated', validators=[oauth2_provider.validators.validate_uris], blank=True)),
                ('client_type', models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], max_length=32)),
                ('authorization_grant_type', models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')], max_length=32)),
                ('client_secret', models.CharField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='oauth2_provider_application')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('code', models.CharField(db_index=True, max_length=255)),
                ('expires', models.DateTimeField()),
                ('redirect_uri', models.CharField(max_length=255)),
                ('scope', models.TextField(blank=True)),
                ('application', models.ForeignKey(to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('token', models.CharField(db_index=True, max_length=255)),
                ('access_token', models.OneToOneField(related_name='refresh_token', to='oauth2_provider.AccessToken')),
                ('application', models.ForeignKey(to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='application',
            field=models.ForeignKey(to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
