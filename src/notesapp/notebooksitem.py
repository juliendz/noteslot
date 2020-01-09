# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notes Table View Sub class
"""
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QMenu, QAction
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem
from notesapp.notes import Notes
from notesapp import notesapp_rc


class NotebooksItem(QStandardItem):

    def __init__(self, parent=None):
        super(NotebooksItem, self).__init__(parent)

    def contextMenuEvent(self, event):
        ctxtmenu = QMenu(self)

        newnote_action = QAction(
            QIcon(':/icons/resources/icons/folder.png'), "New Note", self)
        newnote_action.triggered.connect(self.on_new_note)

        ctxtmenu.addAction(newnote_action)
        ctxtmenu.exec_(event.globalPos())
