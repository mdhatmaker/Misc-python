#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""OpusLib constants."""

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


import opuslib


APPLICATION_TYPES_MAP = {
    'voip': opuslib.api.constants.APPLICATION_VOIP,
    'audio': opuslib.api.constants.APPLICATION_AUDIO,
    'restricted_lowdelay':
        opuslib.api.constants.APPLICATION_RESTRICTED_LOWDELAY,
}
