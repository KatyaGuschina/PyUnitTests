# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Task.title'
        db.delete_column(u'training_task', 'title')


    def backwards(self, orm):
        # Adding field 'Task.title'
        db.add_column(u'training_task', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True),
                      keep_default=False)


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