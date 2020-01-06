# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Note model 
"""


class Note:
    def __init__(self, id:int, parent_id:int, title: str):
        self.id = id
        self.title = title
        self.parent_id = parent_id
        