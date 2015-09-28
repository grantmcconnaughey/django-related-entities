# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedEntity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=255, blank=True)),
                ('primary_object_id', models.PositiveIntegerField()),
                ('related_object_id', models.PositiveIntegerField()),
                ('primary_content_type', models.ForeignKey(related_name='+', to='contenttypes.ContentType')),
                ('related_content_type', models.ForeignKey(related_name='+', to='contenttypes.ContentType')),
            ],
        ),
    ]
