#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""OpusLib Package."""

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


import ctypes  # NOQA

from ctypes.util import find_library  # NOQA


lib_location = find_library('opus')

if lib_location is None:
    raise Exception(
        'Could not find opus library. Make sure it is installed.')

libopus = ctypes.CDLL(lib_location)

c_int_pointer = ctypes.POINTER(ctypes.c_int)
c_int16_pointer = ctypes.POINTER(ctypes.c_int16)
c_float_pointer = ctypes.POINTER(ctypes.c_float)
