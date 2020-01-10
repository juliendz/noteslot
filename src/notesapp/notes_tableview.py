# -*- coding: utf-8 -*-
__license__ = 'GPL v3'
__copyright__ = '2020, Julien Dcruz juliendcruz@gmail.com'
__docformat__ = 'restructuredtext en'

"""
Notes Table View Sub class
"""
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Signal, Slot, QItemSelectionModel, QSize
from PySide2.QtWidgets import QMenu, QAction, QAbstractItemView, QHeaderView
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem, QPixmap
from notesapp.notes import Notes
from notesapp import notesapp_rc


class NotesTableView(QtWidgets.QTableView):

    open_note = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(NotesTableView, self).__init__(parent)

        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setIconSize(QSize(28, 28))

        # Init the view model
        self._vm = QStandardItemModel(0, 2)
        self._vm.setColumnCount(2)
        self._vm.setHeaderData(0, QtCore.Qt.Horizontal, "Note")
        self._vm.setHeaderData(1, QtCore.Qt.Horizontal, "Last Changed")
        self.setModel(self._vm)

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setShowGrid(False)

        self._vm.dataChanged.connect(self.editNoteTitle)
        self.doubleClicked.connect(self.on_double_clicked)

        self._sm = QItemSelectionModel(self._vm)
        self.setSelectionModel(self._sm)

        self._nts = Notes()

        self._curr_nbid = 0

    def get_current_selected_note_id(self):
        selected = self.selectedIndexes()
        selected_id = selected[0].data(QtCore.Qt.UserRole + 1)
        return selected_id

    @Slot(int)
    def editNoteTitle(self, toLeft, bottomRighta):
        n_id = toLeft.data(QtCore.Qt.UserRole + 1)
        self._nts.update(n_id, toLeft.data())

    @Slot(int)
    def populate(self, notebook_id=0):
        self._curr_nbid = notebook_id

        self._vm.removeRows(0, self._vm.rowCount())

        notes = self._nts.get_notes(notebook_id)

        for idx, n in enumerate(notes):
            item = QStandardItem(n['title'])
            item.setIcon(QIcon(QPixmap(':/icons/resources/icons/note.png')))
            item.setData(n['id'], QtCore.Qt.UserRole + 1)
            lastChangedItem = QStandardItem('test')
            self._vm.appendRow([item, lastChangedItem])

    @Slot(object)
    def add_note(self, notebook_id):
        title = "New Note"
        item = QStandardItem(title)
        self._vm.appendRow(item)

        n_id = self._nts.add(notebook_id, title)

        item.setData(n_id, QtCore.Qt.UserRole + 1)

    def contextMenuEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid():
            ctxtmenu = QMenu(self)

            open_action = QAction(
                QIcon(':/icons/resources/icons/folder.png'), "Open Note", self)
            open_action.triggered.connect(self.on_open_note)
            ctxtmenu.addAction(open_action)

            edit_action = QAction(
                QIcon(':/icons/resources/icons/folder.png'), "Edit Note", self)
            edit_action.triggered.connect(self.on_edit_note)
            ctxtmenu.addAction(edit_action)

            delete_action = QAction(
                QIcon(':/icons/resources/icons/folder.png'), "Delete Note", self)
            delete_action.triggered.connect(self.on_delete_note)
            ctxtmenu.addAction(delete_action)

            ctxtmenu.exec_(event.globalPos())

    @Slot()
    def on_open_note(self):
        nid = self.get_current_selected_note_id()
        self.open_note.emit(nid)

    @Slot()
    def on_edit_note(self):
        selected = self.selectedIndexes()
        self.edit(selected[0])

    @Slot()
    def on_delete_note(self):
        selected = self.selectedIndexes()
        nid = self.get_current_selected_note_id()
        self._nts.delete(nid)
        self.populate(self._curr_nbid)

    @Slot()
    def on_double_clicked(self):
        nid = self.get_current_selected_note_id()
        self.open_note.emit(nid)
