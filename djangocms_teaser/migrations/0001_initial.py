# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teaser',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('image', models.ImageField(verbose_name='image', blank=True, null=True, upload_to=cms.models.pluginmodel.get_plugin_media_path)),
                ('url', models.CharField(help_text='If present image will be clickable.', blank=True, null=True, max_length=255, verbose_name='link')),
                ('description', models.TextField(verbose_name='description', blank=True, null=True)),
                ('page_link', models.ForeignKey(help_text='If present image will be clickable', blank=True, verbose_name='page', to='cms.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
