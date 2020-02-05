#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OpusLib Python Module.

"""
OpusLib Python Module.
~~~~~~~

Python bindings to the libopus, IETF low-delay audio codec

:author: Никита Кузнецов <self@svartalf.info>
:copyright: Copyright (c) 2012, SvartalF
:license: BSD 3-Clause License
:source: <https://github.com/onbeep/opuslib>

"""

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


import logging  # NOQA

from .classes import Encoder, Decoder  # NOQA

# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        """Default logging handler to avoid "No handler found" warnings."""
        def emit(self, record):
            """Default logging handler to avoid "No handler found" warnings."""
            pass

logging.getLogger(__name__).addHandler(NullHandler())
