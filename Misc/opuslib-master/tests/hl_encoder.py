#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for a high-level Decoder object"""

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


import unittest

#from opuslib.encoder import Encoder
from opuslib import Encoder
from opuslib.exceptions import OpusError
from opuslib.api import constants


class EncoderTest(unittest.TestCase):

    def test_create(self):
        try:
            Encoder(1000, 3, constants.APPLICATION_AUDIO)
        except OpusError as e:
            self.assertEqual(e.code, constants.BAD_ARG)

        Encoder(48000, 2, constants.APPLICATION_AUDIO)

    def test_reset_state(self):
        encoder = Encoder(48000, 2, constants.APPLICATION_AUDIO)
        encoder.reset_state()
