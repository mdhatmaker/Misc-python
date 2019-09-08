#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


import opuslib.api


class OpusError(Exception):

    def __init__(self, code):
        self.code = code

    def __str__(self):
        return opuslib.api.info.strerror(self.code)
