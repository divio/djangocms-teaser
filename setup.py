#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_teaser import __version__

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='djangocms-teaser',
    version=__version__,
    description='Teaser plugin for django CMS',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/divio/djangocms-teaser',
    packages=['djangocms_teaser', 'djangocms_teaser.migrations', 'djangocms_teaser.migrations_django'],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False
)
