# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Time related helper functions
"""
from PySide2 import QtCore
from PySide2.QtCore import QDateTime
from noteslot.constants import DATETIME_FORMAT, TIME_FORMAT


def get_curr_fmt_ts():
    dt = QDateTime.currentDateTimeUtc()
    dtStr = dt.toString(DATETIME_FORMAT)
    return dtStr


def get_local_fmt_ts(utc_fmt_ts):
    dt = QDateTime.fromString(utc_fmt_ts, DATETIME_FORMAT)
    dt.setTimeSpec(QtCore.Qt.UTC)
    local_dt = dt.toLocalTime()
    curr_dt = QDateTime.currentDateTime()
    print(curr_dt)
    print(local_dt)
    if curr_dt.date() == local_dt.date():
        return "%s %s" % ("Today", local_dt.toString(TIME_FORMAT))
    return local_dt.toString(DATETIME_FORMAT)
