"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Signal, Slot, QSize
from PySide2.QtWidgets import QMainWindow, QApplication, QTableView, QFileDialog, QMessageBox
from PySide2.QtGui import QStandardItemModel, QStandardItem, QPixmap
from noteslot.constants import APP_VERSION, AUTHORS, COPYRIGHT
from noteslot.notebooks import Notebooks
from noteslot.notes import Notes
from noteslot.notebooks_listview import NotebooksListView
from noteslot.notes_tableview import NotesTableView
from noteslot.update_manager import UpdateManager
from noteslot.ui.ui_mainwindow import Ui_MainWindow
from noteslot.note_window import NoteWindow
from noteslot import noteslot_rc


class MainWindow(QMainWindow, Ui_MainWindow):

    populate_search_results = Signal(object)

    _update_mgr = None

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

        # self.statusbar.showMessage("Total: 32 notes")

    def open_pinned_notes(self):
        nts = Notes()
        notes = nts.get_notes()
        for idx, n in enumerate(notes):
            if n['pinned'] == 1:
                self.open_note(n['id'])

    def init_icons(self):
        pass

    def setup_connections(self):
        self.listView_notebooks.add_new_note.connect(
            self.tableView_notes.add_note)

        self.listView_notebooks.load_notes.connect(
            self.tableView_notes.populate)

        self.tableView_notes.open_note.connect(self.open_note)

        self.plainTextEdit_search.textChanged.connect(self.search_notes)
        self.populate_search_results.connect(
            self.listView_notebooks.populate_search_results)
        self.btn_clearsearch.clicked.connect(self.clear_search)

        # App menu
        self.action_newnotebook.triggered.connect(
            self.listView_notebooks.add_notebook)
        self.action_exit.triggered.connect(self.close)
        self.action_checkupdates.triggered.connect(self.on_check_updates)
        self.action_about.triggered.connect(self.on_about)

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

    @Slot()
    def search_notes(self):
        sterm = self.plainTextEdit_search.toPlainText()
        self.populate_search_results.emit(sterm)

    @Slot()
    def clear_search(self):
        self.plainTextEdit_search.setPlainText("")

    @Slot(bool)
    def on_check_updates(self, checked):
        if not self._update_mgr:
            self._update_mgr = UpdateManager()
        self._update_mgr.get_updates()

    @Slot(bool)
    def on_about(self, checked):
        aboutBox = QMessageBox()
        aboutBox.setText("Noteslot (v%s)\nAuthor: %s\n%s" %
                         (APP_VERSION, ','.join(AUTHORS), COPYRIGHT))
        aboutBox.exec()

    def sizeHint(self):
        return QSize(550, 550)
