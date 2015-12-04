djangocms-teaser
================

A teaser plugin for django CMS.


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install djangocms-teaser``.
* Add ``'djangocms_teaser'`` to your ``INSTALLED_APPS`` setting.
* If using Django 1.6 and South < 1.0.2 add ``'djangocms_teaser': 'djangocms_teaser.migrations_django',``
  to ``SOUTH_MIGRATION_MODULES``  (or define ``SOUTH_MIGRATION_MODULES`` if it
  does not exist).
* Run ``manage.py migrate djangocms_teaser``.


Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-teaser/
