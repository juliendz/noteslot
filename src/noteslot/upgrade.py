# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Application Version Upgrade module
"""
from packaging.version import Version
from noteslot.log import LOGGER
from noteslot.db import dbmgr


def upgrade_from_previous_versions(cur_version, db_path):
    db = dbmgr(db_path)
    db.connect()

    if cur_version < Version('0.9.1'):
        LOGGER.info('Upgrading from Version:%s to Version:%s' %
                    (cur_version, '0.8.1'))

        query = "UPDATE settings SET value=? WHERE key='VERSION'"
        db.run_query(query, ('0.9.1',))

    if cur_version < Version('1.0.0-beta'):
        LOGGER.info('Upgrading from Version:%s to Version:%s' %
                    (cur_version, '1.0.0-beta'))
        queries = [
            'ALTER TABLE notes ADD mtime TEXT;'
        ]
        for query in queries:
            db.run_query(query)

        query = "UPDATE settings SET value=? WHERE key='VERSION'"
        db.run_query(query, ('1.0.0-beta',))

    db.disconnect()
    return
