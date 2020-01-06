# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Application Data Initialization 
"""
from PySide2 import QtCore
from notesapp.constants import USER_APPDATA_DIR, APP_NAME, DB_NAME, APP_VERSION
from notesapp.exceptions import AppDataDirReadWriteFailed


def init_app_data_dir():
    data_dir_path = '%s/%s' % (USER_APPDATA_DIR, APP_NAME)
    dir = QtCore.QDir(data_dir_path)
    if not dir.exists(data_dir_path):
        roaming_dir = QtCore.QDir(USER_APPDATA_DIR)
        if not roaming_dir.mkdir(APP_NAME):
            LOGGER.critical(
                'Unable to access or create application data location: %s' % data_dir_path)
            raise AppDataDirReadWriteFailed


def init_app_db():
    from notesapp.db import dbmgr
    db_file = QtCore.QFileInfo(
        "%s/%s/%s" % (USER_APPDATA_DIR, APP_NAME, DB_NAME))
    if not db_file.exists():
        db = dbmgr(db_file.absoluteFilePath())
        db.create_db_from_schema()

        # Add the current version info
        db = dbmgr(db_file.absoluteFilePath())
        db.connect()
        query = 'INSERT INTO settings (key, value) VALUES (?, ?)'
        params = ('VERSION', APP_VERSION)
        db.run_insert_query(query, params)
        db.disconnect()