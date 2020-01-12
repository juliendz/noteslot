# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Time related helper functions
"""
from PySide2 import QtCore
from PySide2.QtCore import QDateTime
from noteslot.constants import TIME_FORMAT


def get_curr_fmt_ts():
    dt = QDateTime.currentDateTimeUtc()
    dtStr = dt.toString(TIME_FORMAT)
    return dtStr


def get_local_fmt_ts(utc_fmt_ts):
    dt = QDateTime.fromString(utc_fmt_ts, TIME_FORMAT)
    return dt.toTimeSpec(QtCore.Qt.LocalTime).toString(TIME_FORMAT)
