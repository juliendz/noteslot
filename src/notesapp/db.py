"""
Description: Database Manager
Started by: Julien Dcruz
Contributors: ...
"""


import sqlite3
from .log import LOGGER


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class dbmgr(object):
    errcode = None
    dbpath = None
    conn = None
    is_open = False

    schema = """
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS `notebooks` (
                    "id" INTEGER PRIMARY KEY ,
                    "title" TEXT NOT NULL  DEFAULT (null)
        );
        CREATE TABLE IF NOT EXISTS `notes` (
                    "id" INTEGER PRIMARY KEY ,
                    "parent_id" INTEGER NOT NULL,
                    "title" TEXT NOT NULL  DEFAULT (null) ,
                    "context" TEXT DEFAULT NULL ,
                    "width" INTEGER DEFAULT NULL ,
                    "height" INTEGER DEFAULT NULL ,
                    "pos_x" INTEGER DEFAULT NULL ,
                    "pos_y" INTEGER DEFAULT NULL ,
        FOREIGN KEY(`parent_id`) REFERENCES `notebooks`(`id`) ON DELETE CASCADE 
        );
        CREATE TABLE IF NOT EXISTS `settings` ( 
                    `key` TEXT UNIQUE,
                    `value` TEXT 
        );
        INSERT INTO notebooks (id, title) VALUES(0, "All Notes");
    """

    def __init__(self, db_path):
        self.dbpath = db_path

    def create_db_from_schema(self):
        try:
            self.connect()
            self.conn.cursor().executescript(self.schema)
            self.disconnect()
        except sqlite3.OperationalError as msg:
            LOGGER.critical('[Error while creating database]: %s' % msg)

    def connect(self):
        if not self.is_open:
            self.conn = sqlite3.connect(self.dbpath)
            self.conn.execute("PRAGMA foreign_keys = 1")
            self.is_open = True

    def disconnect(self):
        self.conn.close()
        self.is_open = False

    def commit(self):
        self.conn.commit()

    def run_insert_query(self, query, params, commit=True):
        """
            Description: Executes an insert sql query using Pythons DB-API (Parameter substitution)
            Arguments: 'query': The sql query string
                       'params' : tuple containing parameters
            """
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, params)
            if commit:
                self.conn.commit()
        except sqlite3.OperationalError as msg:
            LOGGER.error('[DB]: %s' % msg)
        except sqlite3.IntegrityError as msg:
            LOGGER.debug('[DB]: %s : %s : %s' % (msg, query, params))
            LOGGER.error('[DB]: %s : %s' % (msg, params))
        return cursor.lastrowid

    def run_query(self, query, params=(), commit=True):
        """
        Description: Executes an update/delete sql query using Pythons DB-API (Parameter substitution)
            Arguments: query: The sql query string
                       'params' : tuple containing parameters
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, params)
            if commit:
                self.conn.commit()
        except sqlite3.OperationalError as msg:
            LOGGER.error('[DB]: %s' % msg)
        except sqlite3.IntegrityError as msg:
            LOGGER.debug('[DB]: %s : %s : %s' % (msg, query, params))
            LOGGER.error('[DB]: %s : %s' % (msg, params))

        return cursor.rowcount

    def run_select_query(self, query, params=()):
        """
            Description: Executes an select sql query using Pythons DB-API (Parameter substitution)
            Arguments: 'query: The sql query string
                       'params' : tuple containing parameters
            # Returns: False on failure | list[row_number][column_name] on success
        """
        self.conn.row_factory = dict_factory

        cursor = self.conn.cursor()
        try:
            cursor.execute(query, params)
        except sqlite3.OperationalError as msg:
            LOGGER.error('[DB]: %s' % msg)

        data = cursor.fetchall()
        return data
