#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals


class BaseFormat(object):
    """
    Base format class.

    Supported formats are: ogg, avi, mkv, webm, flv, mov, mp4, mpeg
    """

    format_name = None
    ffmpeg_format_name = None

    def parse_options(self, opt):
        if 'format' not in opt or opt.get('format') != self.format_name:
            raise ValueError('invalid Format format')
        return ['-f', self.ffmpeg_format_name]


class RawvideoFormat(BaseFormat):
    """
    Rawvideo equal to no container, mostly used for media analyses.
    """
    format_name = 'rawvideo'
    ffmpeg_format_name = 'rawvideo'


class OggFormat(BaseFormat):
    """
    Ogg container format, mostly used with Vorbis and Theora.
    """
    format_name = 'ogg'
    ffmpeg_format_name = 'ogg'


class AviFormat(BaseFormat):
    """
    Avi container format, often used vith DivX video.
    """
    format_name = 'avi'
    ffmpeg_format_name = 'avi'


class MkvFormat(BaseFormat):
    """
    Matroska format, often used with H.264 video.
    """
    format_name = 'mkv'
    ffmpeg_format_name = 'matroska'


class WebmFormat(BaseFormat):
    """
    WebM is Google's variant of Matroska containing only
    VP8 for video and Vorbis for audio content.
    """
    format_name = 'webm'
    ffmpeg_format_name = 'webm'


class FlvFormat(BaseFormat):
    """
    Flash Video container format.
    """
    format_name = 'flv'
    ffmpeg_format_name = 'flv'


class BaseMovMp4Format(BaseFormat):
    """
    Base MOV/MP4 format class.

    Supported formats are: mov, mp4
    """

    def parse_options(self, opt):
        opt_list = super(BaseMovMp4Format, self).parse_options(opt)
        if opt.get('faststart'):
            opt_list = ['-movflags', 'faststart'] + opt_list
        return opt_list


class MovFormat(BaseMovMp4Format):
    """
    Mov container format, used mostly with H.264 video
    content, often for mobile platforms.
    """
    format_name = 'mov'
    ffmpeg_format_name = 'mov'


class Mp4Format(BaseMovMp4Format):
    """
    Mp4 container format, the default Format for H.264
    video content.
    """
    format_name = 'mp4'
    ffmpeg_format_name = 'mp4'


class MpegFormat(BaseFormat):
    """
    MPEG(TS) container, used mainly for MPEG 1/2 video codecs.
    """
    format_name = 'mpg'
    ffmpeg_format_name = 'mpegts'


class Mp3Format(BaseFormat):
    """
    Mp3 container, used audio-only mp3 files
    """
    format_name = 'mp3'
    ffmpeg_format_name = 'mp3'


class WavFormat(BaseFormat):
    """
    WAV container, audio files
    """
    format_name = 'wav'
    ffmpeg_format_name = 'wav'


class HLSFormat(BaseFormat):
    """
    ts container, segments
    """
    format_name = 'hls'
    ffmpeg_format_name = 'segment'

    def parse_options(self, opt):
        if 'format' not in opt or opt.get('format') != self.format_name:
            raise ValueError('invalid Format format')

        optlist = []
        optlist.extend(['-dn'])
        optlist.extend(['-f', self.ffmpeg_format_name])
        if 'flags' in opt:
            optlist.extend(['-flags', str(opt.get('flags'))])
        if 'segment_list' in opt:
            optlist.extend(['-segment_list', str(opt.get('segment_list'))])
        if 'segment_time' in opt:
            optlist.extend(['-segment_time', str(opt.get('segment_time'))])
        if 'segment_format' in opt:
            optlist.extend(['-segment_format', str(opt.get('segment_format'))])
        if 'segment_list_type' in opt:
            optlist.extend(['-segment_list_type', str(opt.get('segment_list_type'))])

        return optlist


format_list = [
    RawvideoFormat, OggFormat, AviFormat, MkvFormat, WebmFormat, FlvFormat,
    MovFormat, Mp4Format, MpegFormat, Mp3Format, WavFormat, HLSFormat
]
