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
    # Upgrade code to Version(0.9.1)
    # if cur_version < Version('0.9.1'):
    #     LOGGER.info('Upgrading from Version:%s to Version:%s' %
    #                 (cur_version, '0.8.1'))

    #     queries = [
    #         'CREATE TEMPORARY TABLE scan_img_backup(a,b,c,d,e,f,g,h);',
    #         """INSERT INTO scan_img_backup
    #            SELECT id, abspath, name, thumb, sdid, mtime, integrity_check, serial FROM scan_img;
    #         """,
    #         'DROP TABLE scan_img;',
    #         """CREATE TABLE IF NOT EXISTS "scan_img" (
    #             `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #             `abspath` TEXT NOT NULL UNIQUE,
    #             `name` TEXT NOT NULL,
    #             `thumb` BLOB NOT NULL,
    #             `sdid` INTEGER NOT NULL DEFAULT 0,
    #             `mtime` INTEGER,
    #             `integrity_check` INTEGER,
    #             `serial` INTEGER,
    #             FOREIGN KEY(`sdid`) REFERENCES `scan_dir`(`id`) ON DELETE CASCADE )
    #         """,
    #         'INSERT INTO scan_img SELECT a,b,c,d,e,f,g,h FROM scan_img_backup;',
    #         'DROP TABLE scan_img_backup;',
    #     ]

    #     for query in queries:
    #         db.run_query(query)
    #     db.commit()

    #     cur_version = Version('0.8.1')

    db.disconnect()
    return
