# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Static and runtime constants
"""

from PySide2 import QtCore
from enum import Enum
from .exceptions import OsNotDetectedError
import platform

APP_NAME = 'noteslot'
HUMAN_APP_NAME = 'NoteApp - A sticky notes application'
APP_VERSION = '0.9.0'
DB_NAME = '%s.db' % APP_NAME
LOG_FILE = '%s.log' % APP_NAME
USER_APPDATA_DIR = QtCore.QStandardPaths.writableLocation(
    QtCore.QStandardPaths.AppDataLocation)


class SortMode(Enum):
    CreationTime = 1
    RecentChanges = 2
    Name = 3
    Size = 4


class ScrollDirection(Enum):
    Up = 1
    Down = 2


class OSType(Enum):
    OS_WINDOWS = 1
    OS_LINUX = 2


def get_appdata_dir() -> OSType:
    if platform.system() == 'Windows':
        return OSType.OS_WINDOWS
    if platform.system() == 'Linux':
        return OSType.OS_LINUX
    raise OsNotDetectedError
