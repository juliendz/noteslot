# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notebook model 
"""


class Notebook:
    def __init__(self, id:int, title: str):
        self.id = id
        self.title = title