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
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap
from notesapp.notebooks import Notebooks
from notesapp import notesapp_rc


class NotebooksListView(QtWidgets.QListView):

    load_notes = QtCore.Signal(int, str)
    add_new_note = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(NotebooksListView, self).__init__(parent)
        self.setIconSize(QSize(28, 28))

        self._vm = QStandardItemModel()
        self._vm.setColumnCount(1)
        self.setModel(self._vm)

        self._sm = QItemSelectionModel(self._vm)
        self.setSelectionModel(self._sm)

        self._nbs = Notebooks()

        self._sm.selectionChanged.connect(self.on_selection_changed)

        self._vm.dataChanged.connect(self.editNotebookTitle)

        self._search_term = ""

    def add_item(self, nb, insertFirst=False):
        item = QStandardItem(nb['title'])
        item.setIcon(
            QIcon(QPixmap(':/icons/resources/icons/notebook.png')))
        f = item.font()
        f.setBold(True)
        f.setPointSize(10)
        item.setFont(f)
        item.setData(nb['id'], QtCore.Qt.UserRole + 1)
        if not insertFirst:
            self._root_item.appendRow(item)
        else:
            self._root_item.insertRow(0, [item])

    def populate(self):

        self._vm.clear()
        self._root_item = self._vm.invisibleRootItem()

        notebooks = self._nbs.get()

        for idx, nb in enumerate(notebooks):
            self.add_item(nb)

    def set_selection(self, index=None):
        self.clearSelection()
        if not index:
            self._sm.select(
                self._vm.index(0, 0),
                QItemSelectionModel.Select | QItemSelectionModel.Rows
            )
        else:
            self._sm.select(
                index,
                QItemSelectionModel.Select | QItemSelectionModel.Rows
            )

    def on_selection_changed(self, selected, deselected):
        print(self.get_current_selected_notebook_id())
        self.load_notes.emit(
            self.get_current_selected_notebook_id(), self._search_term)

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

    def get_current_selection(self):
        return self.selectedIndexes()

    @Slot(object)
    def add_notebook(self):
        n = {}
        n['title'] = "New Notebook"
        nb_id = self._nbs.add(n['title'])
        n['id'] = nb_id
        self.add_item(n)

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

    @Slot(object)
    def populate_search_results(self, sterm):
        self._search_term = sterm
        if sterm != "":
            if self._vm.index(0, 0).data(QtCore.Qt.UserRole + 1) != -1:
                self._prev_selection = self.selectedIndexes()[0]
                self.add_item({"title": 'Search results', "id": -1}, True)
            self.set_selection(self._vm.indexFromItem(
                self._root_item.child(0, 0)))
        else:
            if self._vm.index(0, 0).data(QtCore.Qt.UserRole + 1) == -1:
                self._vm.removeRow(0)
            self.set_selection(self._prev_selection)

    def sizeHint(self):
        return QSize(100, 350)

    # def minimumSizeHint(self):
        # return QSize(20, 16777215)
