#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""High-level interface to a opus decoder functions"""

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


import opuslib.api.decoder
import opuslib.api.encoder
import opuslib.api.ctl
import opuslib.constants


class Decoder(object):

    def __init__(self, fs, channels):
        """
        Parameters:
            fs : sampling rate
            channels : number of channels
        """

        self._fs = fs
        self._channels = channels
        self._state = opuslib.api.decoder.create(fs, channels)

    def __del__(self):
        if hasattr(self, '_state'):
            # Destroying state only if __init__ completed successfully
            opuslib.api.decoder.destroy(self._state)

    def reset_state(self):
        """
        Resets the codec state to be equivalent to a freshly initialized state
        """

        opuslib.api.decoder.opuslib.api.ctl(
            self._state, opuslib.api.ctl.reset_state)

    def decode(self, data, frame_size, decode_fec=False):
        return opuslib.api.decoder.decode(
            self._state, data, len(data), frame_size, decode_fec,
            channels=self._channels)

    def decode_float(self, data, frame_size, decode_fec=False):
        return opuslib.api.decoder.decode_float(
            self._state, data, len(data), frame_size, decode_fec,
            channels=self._channels)

    # CTL interfaces

    _get_final_range = lambda self: opuslib.api.decoder.opuslib.api.ctl(
        self._state, opuslib.api.ctl.get_final_range)

    final_range = property(_get_final_range)

    _get_bandwidth = lambda self: opuslib.api.decoder.opuslib.api.ctl(
        self._state, opuslib.api.ctl.get_bandwidth)

    bandwidth = property(_get_bandwidth)

    _get_pitch = lambda self: opuslib.api.decoder.opuslib.api.ctl(
        self._state, opuslib.api.ctl.get_pitch)

    pitch = property(_get_pitch)

    _get_lsb_depth = lambda self: opuslib.api.decoder.opuslib.api.ctl(
        self._state, opuslib.api.ctl.get_lsb_depth)

    _set_lsb_depth = lambda self, x: opuslib.api.decoder.opuslib.api.ctl(
        self._state, opuslib.api.ctl.set_lsb_depth, x)

    lsb_depth = property(_get_lsb_depth, _set_lsb_depth)

    _get_gain = lambda self: opuslib.api.decoder.opuslib.api.ctl(
        self._state, opuslib.api.ctl.get_gain)

    _set_gain = lambda self, x: opuslib.api.decoder.opuslib.api.ctl(
        self._state, opuslib.api.ctl.set_gain, x)

    gain = property(_get_gain, _set_gain)


class Encoder(object):

    def __init__(self, fs, channels, application):
        """
        Parameters:
            fs : sampling rate
            channels : number of channels
        """

        if application in opuslib.constants.APPLICATION_TYPES_MAP.keys():
            application = opuslib.constants.APPLICATION_TYPES_MAP[application]
        elif application in opuslib.constants.APPLICATION_TYPES_MAP.values():
            pass  # Nothing to do here
        else:
            raise ValueError(
                "`application` value must be in 'voip', 'audio' or "
                "'restricted_lowdelay'")

        self._fs = fs
        self._channels = channels
        self._application = application
        self._state = opuslib.api.encoder.create(fs, channels, application)

    def __del__(self):
        if hasattr(self, '_state'):
            # Destroying state only if __init__ completed successfully
            opuslib.api.encoder.destroy(self._state)

    def reset_state(self):
        """
        Resets the codec state to be equivalent to a freshly initialized state
        """

        opuslib.api.encoder.ctl(
            self._state, opuslib.api.ctl.reset_state)

    def encode(self, data, frame_size):
        return opuslib.api.encoder.encode(
            self._state, data, frame_size, len(data))

    def encode_float(self, data, frame_size, decode_fec=False):
        return opuslib.api.encoder.encode_float(
            self._state, data, frame_size, len(data))

    # CTL interfaces

    _get_final_range = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_final_range)

    final_range = property(_get_final_range)

    _get_bandwidth = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_bandwidth)

    bandwidth = property(_get_bandwidth)

    _get_pitch = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_pitch)

    pitch = property(_get_pitch)

    _get_lsb_depth = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_lsb_depth)

    _set_lsb_depth = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_lsb_depth, x)

    lsb_depth = property(_get_lsb_depth, _set_lsb_depth)

    _get_complexity = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_complexity)

    _set_complexity = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_complexity, x)

    complexity = property(_get_complexity, _set_complexity)

    _get_bitrate = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_bitrate)

    _set_bitrate = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_bitrate, x)

    bitrate = property(_get_bitrate, _set_bitrate)

    _get_vbr = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_vbr)

    _set_vbr = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_vbr, x)

    vbr = property(_get_vbr, _set_vbr)

    _get_vbr_constraint = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_vbr_constraint)

    _set_vbr_constraint = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_vbr_constraint, x)

    vbr_constraint = property(_get_vbr_constraint, _set_vbr_constraint)

    _get_force_channels = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_force_channels)

    _set_force_channels = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_force_channels, x)

    force_channels = property(_get_force_channels, _set_force_channels)

    _get_max_bandwidth = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_max_bandwidth)

    _set_max_bandwidth = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_max_bandwidth, x)

    max_bandwidth = property(_get_max_bandwidth, _set_max_bandwidth)

    _set_bandwidth = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_bandwidth, x)

    bandwidth = property(None, _set_bandwidth)

    _get_signal = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_signal)

    _set_signal = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_signal, x)

    signal = property(_get_signal, _set_signal)

    _get_application = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_application)

    _set_application = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_application, x)

    application = property(_get_application, _set_application)

    _get_sample_rate = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_sample_rate)

    sample_rate = property(_get_sample_rate)

    _get_lookahead = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_lookahead)

    lookahead = property(_get_lookahead)

    _get_inband_fec = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_inband_fec)

    _set_inband_fec = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.set_inband_fec)

    inband_fec = property(_get_inband_fec, _set_inband_fec)

    _get_packet_loss_perc = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_packet_loss_perc)

    _set_packet_loss_perc = \
        lambda self, x: opuslib.api.encoder.ctl(
            self._state, opuslib.api.ctl.set_packet_loss_perc, x)

    packet_loss_perc = property(_get_packet_loss_perc, _set_packet_loss_perc)

    _get_dtx = lambda self: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_dtx)

    _set_dtx = lambda self, x: opuslib.api.encoder.ctl(
        self._state, opuslib.api.ctl.get_dtx, x)
