# -*- coding: utf-8 -*-
import os.path
from setuptools import setup, find_packages

pkg_name = 'djangovoice'
version = __import__(pkg_name).__version__
description = file('README.rst', 'r').read()

# get requires from requirements/global.txt file.
requires_file_name = os.path.join(
    os.path.dirname(__file__), 'requirements', 'global.txt')
with file(requires_file_name) as install_requires:
    install_requires = map(lambda x: x.split(), install_requires.readlines())

setup(
    name='django-voice',
    version=version,
    description="A feedback application for Django",
    long_description=description,
    author=u'Gökmen Görgen',
    author_email='gokmen@alageek.com',
    url='https://github.com/gkmngrgn/django-voice',
    license='BSD',
    platforms='any',
    packages=find_packages(exclude=('demo', 'demo.*')),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment"
    ]
)
