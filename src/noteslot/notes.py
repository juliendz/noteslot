# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notebook functions 
"""
from noteslot import settings
from noteslot.db import dbmgr
from noteslot import time


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

    def get_pinned_notes(self):
        self._db.connect()
        query = "SELECT * FROM notes WHERE pinned=1"
        res = self._db.run_select_query(query)
        self._db.disconnect()
        return res

    def get_pinned_notes_count(self):
        self._db.connect()
        query = "SELECT COUNT(*) as pinned_notes_count FROM notes WHERE pinned=1"
        res = self._db.run_select_query(query)
        self._db.disconnect()
        return res[0]['pinned_notes_count']

    def get_by_title(self, title):
        self._db.connect()
        query = "SELECT * FROM notes WHERE title LIKE ?"
        res = self._db.run_select_query(query, ('%'+title+'%',))
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
        mtime = time.get_curr_fmt_ts()
        query = "INSERT INTO notes (parent_id, title, mtime) VALUES (?, ?, ?)"
        self._db.connect()
        res = self._db.run_insert_query(query, (notebook_id, title, mtime))
        self._db.disconnect()
        return res

    def update(self, id, title, content=None, updateContent=False):
        self._db.connect()
        if updateContent:
            mtime = time.get_curr_fmt_ts()
            query = "UPDATE notes SET title=?, content=?, mtime=? WHERE id=?"
            res = self._db.run_query(query, (title, content, mtime, id))
        else:
            query = "UPDATE notes SET title=? WHERE id = ?"
            res = self._db.run_query(query, (title, id))
        self._db.disconnect()
        return res

    def saveSize(self, id, width, height):
        self._db.connect()
        query = "UPDATE notes SET width=?, height=? WHERE id=?"
        res = self._db.run_query(query, (width, height, id))
        self._db.disconnect()
        return res

    def savePos(self, id, x, y):
        self._db.connect()
        query = "UPDATE notes SET pos_x=?, pos_y=? WHERE id=?"
        res = self._db.run_query(query, (x, y, id))
        self._db.disconnect()
        return res

    def saveStatus(self, id, isPinned):
        self._db.connect()
        if isPinned:
            pinned = 1
        else:
            pinned = 0
        query = "UPDATE notes SET pinned=? WHERE id=?"
        res = self._db.run_query(query, (pinned, id))
        self._db.disconnect()
        return res

    def delete(self, note_id):
        self._db.connect()
        query = "DELETE FROM notes WHERE id = ?"
        res = self._db.run_query(query, (note_id,))
        self._db.disconnect()
