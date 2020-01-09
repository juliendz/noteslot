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


class NotesTableView(QtWidgets.QTableView):

    def __init__(self, parent=None):
        super(NotesTableView, self).__init__(parent)

        # Init the view model
        self._vm = QStandardItemModel()
        self._vm.setColumnCount(2)
        self.setModel(self._vm)

        # self._root_item = self._vm.invisibleRootItem()

    @Slot(int)
    def populate(self, notebook_id=0):

        self._vm.clear()
        self._root_item = self._vm.invisibleRootItem()

        nts = Notes()
        notes = nts.get_notes(notebook_id)

        for idx, n in enumerate(notes):
            item = QStandardItem(n['title'])
            item.setData(n['id'], QtCore.Qt.UserRole + 1)
            self._root_item.appendRow(item)

    @Slot(object)
    def add_note(self, notebook_id):
        title = "New Note"
        item = QStandardItem(title)
        self._root_item.appendRow(item)

        nts = Notes()
        n_id = nts.add_note(notebook_id, title)

        item.setData(n_id, QtCore.Qt.UserRole + 1)

    def contextMenuEvent(self, event):

        ctxtmenu = QMenu(self)

        newnote_action = QAction(
            QIcon(':/icons/resources/icons/folder.png'), "New Note", self)
        newnote_action.triggered.connect(self.on_new_note)

        ctxtmenu.addAction(newnote_action)
        ctxtmenu.exec_(event.globalPos())

    @Slot()
    def on_new_note(self):
        print('test')
