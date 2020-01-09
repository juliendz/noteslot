# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notebook List View Sub class
"""
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal, Slot, QItemSelectionModel
from PySide2.QtWidgets import QMenu, QAction
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem
from notesapp.notebooks import Notebooks
from notesapp import notesapp_rc


class NotebooksListView(QtWidgets.QListView):

    load_notes = QtCore.Signal(int)
    add_new_note = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(NotebooksListView, self).__init__(parent)

        self._vm = QStandardItemModel()
        self._vm.setColumnCount(1)
        self.setModel(self._vm)

        self._sm = QItemSelectionModel(self._vm)
        self.setSelectionModel(self._sm)

        self._root_item = self._vm.invisibleRootItem()

        self._sm.selectionChanged.connect(self.on_selection_changed)

    def populate(self):

        nbs = Notebooks()
        notebooks = nbs.get()

        for idx, nb in enumerate(notebooks):
            item = QStandardItem(nb['title'])
            item.setData(nb['id'], QtCore.Qt.UserRole + 1)
            self._root_item.appendRow(item)

    def set_selection(self):
        self._sm.select(
            self._vm.index(0, 0),
            QItemSelectionModel.Select | QItemSelectionModel.Rows
        )

    def on_selection_changed(self, selected, deselected):
        self.load_notes.emit(self.get_current_selected_notebook_id())

    def contextMenuEvent(self, event):

        index = self.indexAt(event.pos())
        if index.isValid():
            ctxtmenu = QMenu(self)
            newnote_action = QAction(
                QIcon(':/icons/resources/icons/folder.png'), "New Note", self)
            newnote_action.triggered.connect(self.on_new_note)
            ctxtmenu.addAction(newnote_action)
            ctxtmenu.exec_(event.globalPos())
        else:
            ctxtmenu = QMenu(self)
            newnotebook_action = QAction(
                QIcon(':/icons/resources/icons/folder.png'), "New Notebook", self)
            newnotebook_action.triggered.connect(self.add_notebook)
            ctxtmenu.addAction(newnotebook_action)
            ctxtmenu.exec_(event.globalPos())

    def get_current_selected_notebook_id(self):
        selected = self.selectedIndexes()
        selected_id = selected[0].data(QtCore.Qt.UserRole + 1)
        print(selected_id)
        return selected_id

    @Slot(object)
    def add_notebook(self):
        title = "New Notebook"
        item = QStandardItem(title)
        self._root_item.appendRow(item)

        nbs = Notebooks()
        nb_id = nbs.add(title)

        item.setData(nb_id, QtCore.Qt.UserRole + 1)

    @Slot()
    def on_new_note(self):
        self.add_new_note.emit(self.get_current_selected_notebook_id())
