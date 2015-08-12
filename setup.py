#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

import setuptools

try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    setup_requires=['pbr'],
    pbr=True)
