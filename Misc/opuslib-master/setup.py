#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""OpusLib Package."""

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


import os
import setuptools
import sys


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist upload')
        sys.exit()


publish()


setuptools.setup(
    name='opuslib',
    version='1.1.0',
    author='Никита Кузнецов',
    author_email='self@svartalf.info',
    maintainer='Orion Labs, Inc.',
    maintainer_email='code@orionlabs.co',
    license='BSD 3-Clause License',
    url='https://github.com/onbeep/opuslib',
    description='Python bindings to the libopus, IETF low-delay audio codec',
    packages=('opuslib', 'opuslib.api'),
    test_suite='tests',
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
    ),
)
