# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notebook functions 
"""
from notesapp import settings
from notesapp.db import dbmgr


class Notes():
    def __init__(self, db_path=settings.get_db_path()):
        self._db = dbmgr(db_path)

    def connect(self):
        self._db.connect()

    def disconnect(self):
        self._db.disconnect()

    def commit(self):
        self._db.commit()

    def get_notes(self, notebook_id=0):
        self._db.connect()
        if notebook_id == 0:
            query = "SELECT * FROM notes"
            res = self._db.run_select_query(query)
        else:
            query = "SELECT * FROM notes WHERE parent_id = ?"
            res = self._db.run_select_query(query, (notebook_id,))
        self._db.disconnect()
        return res

    def get(self, note_id):
        self._db.connect()
        query = "SELECT * FROM notes WHERE id = ?"
        res = self._db.run_select_query(query, (note_id,))
        self._db.disconnect()
        if len(res) > 0:
            return res[0]
        return None

    def add(self, notebook_id, title):
        query = "INSERT INTO notes (parent_id, title) VALUES (?, ?)"
        self._db.connect()
        res = self._db.run_insert_query(query, (notebook_id, title))
        self._db.disconnect()
        return res

    def update(self, id, title, content=None, updateContent=False):
        self._db.connect()
        if not updateContent:
            query = "UPDATE notes SET title=? WHERE id = ?"
            res = self._db.run_query(query, (title, id))
        else:
            query = "UPDATE notes SET title=?, content=? WHERE id=?"
            res = self._db.run_query(query, (title, content, id))
        self._db.disconnect()
        return res
