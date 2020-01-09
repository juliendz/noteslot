# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notebook List View Sub class
"""
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal, Slot, QItemSelectionModel, QSize
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

        self._nbs = Notebooks()

        self._sm.selectionChanged.connect(self.on_selection_changed)

        self._vm.dataChanged.connect(self.editNotebookTitle)

    def populate(self):

        self._vm.clear()
        self._root_item = self._vm.invisibleRootItem()

        notebooks = self._nbs.get()

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

            if index.row() > 0:
                edit_action = QAction(
                    QIcon(':/icons/resources/icons/folder.png'), "Edit Notebook", self)
                edit_action.triggered.connect(self.on_edit_notebook)
                ctxtmenu.addAction(edit_action)

                delete_action = QAction(
                    QIcon(':/icons/resources/icons/folder.png'), "Delete Notebook", self)
                delete_action.triggered.connect(self.on_delete_notebook)
                ctxtmenu.addAction(delete_action)

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
        if len(selected) > 0:
            selected_id = selected[0].data(QtCore.Qt.UserRole + 1)
            return selected_id
        return 0

    @Slot(object)
    def add_notebook(self):
        title = "New Notebook"
        item = QStandardItem(title)
        self._root_item.appendRow(item)

        nb_id = self._nbs.add(title)

        item.setData(nb_id, QtCore.Qt.UserRole + 1)

    @Slot()
    def on_new_note(self):
        self.add_new_note.emit(self.get_current_selected_notebook_id())

    @Slot()
    def on_edit_notebook(self):
        selected = self.selectedIndexes()
        self.edit(selected[0])

    @Slot()
    def on_delete_notebook(self):
        selected = self.selectedIndexes()
        nbid = self.get_current_selected_notebook_id()
        self._nbs.delete(nbid)
        self.populate()

    @Slot(int)
    def editNotebookTitle(self, toLeft, bottomRight):
        nbid = toLeft.data(QtCore.Qt.UserRole + 1)
        self._nbs.update(nbid, toLeft.data())

    def sizeHint(self):
        return QSize(100, 16777215)

    # def minimumSizeHint(self):
        # return QSize(20, 16777215)
