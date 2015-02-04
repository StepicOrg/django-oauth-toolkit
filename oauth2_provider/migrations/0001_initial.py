# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        db.create_table('oauth2_provider_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client_id', self.gf('django.db.models.fields.CharField')(default='S44hG2sEqVUzO1QP5Uu7cYU6a2xoPHNwWpFQclfa', unique=True, db_index=True, max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='oauth2_provider_application', to=orm['users.User'])),
            ('redirect_uris', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('client_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('authorization_grant_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('client_secret', self.gf('django.db.models.fields.CharField')(blank=True, default='4475uiQQPKKsRC25Tlfd9JqnyloSpI5tT0tsmk60Z53bIMpLkcgO730ctsBBtZ1bJej8NxnKaw6gf3SU5q5EKAmSbZvu97c2fclaW4KK8020ucCh3QCBPDHuegO1VDwu', db_index=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('skip_authorization', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('oauth2_provider', ['Application'])

        # Adding model 'Grant'
        db.create_table('oauth2_provider_grant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth2_provider.Application'])),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('redirect_uri', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('scope', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('oauth2_provider', ['Grant'])

        # Adding model 'AccessToken'
        db.create_table('oauth2_provider_accesstoken', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth2_provider.Application'])),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('scope', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('oauth2_provider', ['AccessToken'])

        # Adding model 'RefreshToken'
        db.create_table('oauth2_provider_refreshtoken', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth2_provider.Application'])),
            ('access_token', self.gf('django.db.models.fields.related.OneToOneField')(related_name='refresh_token', unique=True, to=orm['oauth2_provider.AccessToken'])),
        ))
        db.send_create_signal('oauth2_provider', ['RefreshToken'])


    def backwards(self, orm):
        # Deleting model 'Application'
        db.delete_table('oauth2_provider_application')

        # Deleting model 'Grant'
        db.delete_table('oauth2_provider_grant')

        # Deleting model 'AccessToken'
        db.delete_table('oauth2_provider_accesstoken')

        # Deleting model 'RefreshToken'
        db.delete_table('oauth2_provider_refreshtoken')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'oauth2_provider.accesstoken': {
            'Meta': {'object_name': 'AccessToken'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth2_provider.Application']"}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scope': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"})
        },
        'oauth2_provider.application': {
            'Meta': {'object_name': 'Application'},
            'authorization_grant_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_id': ('django.db.models.fields.CharField', [], {'default': "'a7U44PAOr0OBRkdUAp9sN9CbVQWtTIn9GcBPpyZq'", 'unique': 'True', 'db_index': 'True', 'max_length': '100'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'UnuAnaJVbAgIzmE3xoGozjcHjdDPHgwnBI9QiOKP6ttu8HJhTIcg530kHLGCLtBgKyTKkzwGORqvVtDiVQByLbwqZNZIeg0SO7N8YddMx0dRkKGjkzGecnbjBwhb2D1K'", 'db_index': 'True', 'max_length': '255'}),
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'redirect_uris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skip_authorization': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oauth2_provider_application'", 'to': "orm['users.User']"})
        },
        'oauth2_provider.grant': {
            'Meta': {'object_name': 'Grant'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth2_provider.Application']"}),
            'code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redirect_uri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scope': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"})
        },
        'oauth2_provider.refreshtoken': {
            'Meta': {'object_name': 'RefreshToken'},
            'access_token': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'refresh_token'", 'unique': 'True', 'to': "orm['oauth2_provider.AccessToken']"}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth2_provider.Application']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"})
        },
        'users.user': {
            'Meta': {'object_name': 'User'},
            'bit_field': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'calendar_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_registered': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'is_creator': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'is_guest': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'db_index': 'True', 'max_length': '7'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notification_email_delay': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'subscribed_for_mail': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subscribed_for_news_en': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'subscribed_for_news_ru': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unsubscribe_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        }
    }

    complete_apps = ['oauth2_provider']