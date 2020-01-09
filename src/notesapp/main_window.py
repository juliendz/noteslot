"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QTableView, QFileDialog
from PySide2.QtGui import QStandardItemModel, QStandardItem, QPixmap
from notesapp.notebooks import Notebooks
from notesapp.notebooks_listview import NotebooksListView
from notesapp.ui.ui_mainwindow import Ui_MainWindow
from notesapp import notesapp_rc


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_icons()

        self.init_notebooks_listview()

        self.init_notes_tableview()

        self.populate_notebooks()

    def init_icons(self):
        self.label_searchicon.setPixmap(
            QPixmap(':/icons/resources/icons/search.png'))

    def init_notebooks_listview(self):

        self.listView_notebooks = NotebooksListView(self.splitter)
        self.listView_notebooks.setObjectName(u"listView_notebooks")
        self.splitter.addWidget(self.listView_notebooks)

        self._notebooks_vm = QStandardItemModel()
        self._notebooks_vm.setColumnCount(1)
        self.listView_notebooks.setModel(self._notebooks_vm)

        self._root_item = self._notebooks_vm.invisibleRootItem()

    def init_notes_tableview(self):
        self.tableView_notes = QTableView(self.splitter)
        self.tableView_notes.setObjectName(u"tableView_notes")
        self.splitter.addWidget(self.tableView_notes)

    def populate_notebooks(self):
        nbs = Notebooks()
        notebooks = nbs.get_notebooks()

        for idx, nb in enumerate(notebooks):
            item = QStandardItem(nb['title'])
            item.setData(nb['id'], QtCore.Qt.UserRole + 1)
            self._root_item.appendRow(item)
