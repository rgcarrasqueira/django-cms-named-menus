# /usr/bin/env python
import codecs
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='djangocms-named-menus',
    version='2.0.1',
    description='Allows you to add and edit custom named menus similar to Wordpress menus',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Ryan Bagwell, Rogerio Carrasqueira, Michael Carder Ltd',
    license='MIT',
    url='https://github.com/mcldev/djangocms-named-menus',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.11',
        'django-classy-tags',
        'django-cms>=3.3',
        'jsonfield>=1.0.0',
        'django-autoslug>=1.7.2',
    ],
    package_data={
        'readme': ['README.md'],
        'license': ['LICENSE']
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
