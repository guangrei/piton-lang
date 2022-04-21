#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import Bahasa

setup(
    name='Bahasa',
    version=Bahasa.__version__,
    description='python bahasa indonesia.',
    long_description='',
    author=Bahasa.__author__,
    author_email='myawn@pm.me',
    url='https://github.com/guangrei/piton-lang',
    py_modules=['Bahasa'],
    license='MIT',
    platforms='any'
)
