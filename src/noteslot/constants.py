# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Static and runtime constants
"""

from PySide2 import QtCore
from PySide2.QtCore import QDir
from enum import Enum, auto
from .exceptions import OsNotDetectedError
import platform

APP_VERSION = '1.0.0-beta.3'

APP_NAME = 'noteslot'
HUMAN_APP_NAME = 'Noteslot - A sticky notes application'
DB_NAME = '%s.db' % APP_NAME
LOG_FILE = '%s.log' % APP_NAME
USER_APPDATA_DIR = QtCore.QStandardPaths.writableLocation(
    QtCore.QStandardPaths.AppDataLocation)
AUTHORS = ['Julien Dcruz (juliendcruz@gmail.com)']
COPYRIGHT = "Copyright ©2020 Julien Dcruz"

DATETIME_FORMAT = "MMMM dd yyyy, HH:mm"
TIME_FORMAT = "HH:mm"

LOCK_FILE = QDir.temp().absoluteFilePath("noteslot.lock")


class OSType(Enum):
    OS_WINDOWS = 1
    OS_LINUX = 2


class SettingType(Enum):
    CHECK_UPDATE_ON_STARTUP = auto()
    CHECK_UPDATE_URL = auto()


def get_appdata_dir() -> OSType:
    if platform.system() == 'Windows':
        return OSType.OS_WINDOWS
    if platform.system() == 'Linux':
        return OSType.OS_LINUX
    raise OsNotDetectedError
