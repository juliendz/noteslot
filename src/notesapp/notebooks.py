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

    def get(self):
        query = "SELECT * FROM notebooks"
        self._db.connect()
        res = self._db.run_select_query(query)
        self._db.disconnect()
        return res

    def add(self, title):
        query = "INSERT INTO notebooks (title) VALUES (?)"
        self._db.connect()
        res = self._db.run_insert_query(query, (title, ))
        self._db.disconnect()
        return res

    def update(self, id, title):
        self._db.connect()
        query = "UPDATE notebooks SET title=? WHERE id = ?"
        res = self._db.run_query(query, (title, id))
        self._db.disconnect()
        return res

    def delete(self, notebook_id):
        self._db.connect()
        query = "DELETE FROM notebooks WHERE id = ?"
        res = self._db.run_query(query, (notebook_id,))
        self._db.disconnect()
