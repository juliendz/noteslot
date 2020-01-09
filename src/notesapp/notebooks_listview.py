# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notebook List View Sub class 
"""
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMenu, QAction

class NotebooksListView(QtWidgets.QListView):

    def __init__(self, parent=None):
        super(NotebooksListView, self).__init__(parent)
    
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        action_add = QAction("New Note")