# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.result'
        db.add_column(u'training_task', 'result',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=10000, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.result'
        db.delete_column(u'training_task', 'result')


    models = {
        u'training.task': {
            'Meta': {'object_name': 'Task'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'})
        }
    }

    complete_apps = ['training']