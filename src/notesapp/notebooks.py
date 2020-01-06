# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notebook functions 
"""
from notesapp import settings
from notesapp.db import dbmgr

class Notebooks():
    def __init__(self, db_path=settings.get_db_path()):
        self._db = dbmgr(db_path)

    def connect(self):
        self._db.connect()

    def disconnect(self):
        self._db.disconnect()

    def commit(self):
        self._db.commit()

    def get_notebooks(self):
        query = "SELECT * FROM notebooks"
        self._db.connect()
        res = self._db.run_select_query(query)
        self._db.disconnect()
        return res