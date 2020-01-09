"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QMainWindow, QApplication, QTableView, QFileDialog
from PySide2.QtGui import QStandardItemModel, QStandardItem, QPixmap
from notesapp.notebooks import Notebooks
from notesapp.notebooks_listview import NotebooksListView
from notesapp.notes_tableview import NotesTableView
from notesapp.ui.ui_mainwindow import Ui_MainWindow
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
        # self.tableView_notes.populate()

    def init_icons(self):
        self.label_searchicon.setPixmap(
            QPixmap(':/icons/resources/icons/search.png'))

    def setup_connections(self):
        self.listView_notebooks.add_new_note.connect(
            self.tableView_notes.add_note)

        self.listView_notebooks.load_notes.connect(
            self.tableView_notes.populate)

    Slot()

    def test(self):
        print('sc')

    def init_notebooks_listview(self):
        self.listView_notebooks = NotebooksListView(self.splitter)
        self.splitter.addWidget(self.listView_notebooks)

    def init_notes_tableview(self):
        self.tableView_notes = NotesTableView(self.splitter)
        self.splitter.addWidget(self.tableView_notes)
