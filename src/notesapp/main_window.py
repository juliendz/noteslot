"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Signal, Slot, QSize
from PySide2.QtWidgets import QMainWindow, QApplication, QTableView, QFileDialog
from PySide2.QtGui import QStandardItemModel, QStandardItem, QPixmap
from notesapp.notebooks import Notebooks
from notesapp.notes import Notes
from notesapp.notebooks_listview import NotebooksListView
from notesapp.notes_tableview import NotesTableView
from notesapp.ui.ui_mainwindow import Ui_MainWindow
from notesapp.note_window import NoteWindow
from notesapp import notesapp_rc


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.init_icons()

        self.init_notebooks_listview()
        self.init_notes_tableview()

        self.setup_connections()

        self.listView_notebooks.populate()
        self.listView_notebooks.set_selection()

        self._open_notes = {}
        self.open_pinned_notes()

    def open_pinned_notes(self):
        nts = Notes()
        notes = nts.get_notes()
        for idx, n in enumerate(notes):
            if n['pinned'] == 1:
                self.open_note(n['id'])

    def init_icons(self):
        self.label_searchicon.setPixmap(
            QPixmap(':/icons/resources/icons/search.png'))

    def setup_connections(self):
        self.listView_notebooks.add_new_note.connect(
            self.tableView_notes.add_note)

        self.listView_notebooks.load_notes.connect(
            self.tableView_notes.populate)

        self.tableView_notes.open_note.connect(self.open_note)

    def init_notebooks_listview(self):
        self.listView_notebooks = NotebooksListView(self.splitter)
        self.splitter.addWidget(self.listView_notebooks)

    def init_notes_tableview(self):
        self.tableView_notes = NotesTableView(self.splitter)
        self.splitter.addWidget(self.tableView_notes)

    @Slot(int)
    def open_note(self, note_id):
        nw = NoteWindow(note_id)
        nw.closed.connect(self.close_note)
        self._open_notes[note_id] = nw
        nw.show()

    @Slot(int)
    def close_note(self, note_id):
        self._open_notes.pop(note_id, None)

    def sizeHint(self):
        return QSize(550, 550)

    def resizeEvent(self, event):
        print(event)
