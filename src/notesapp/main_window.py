"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide2.QtGui import QStandardItemModel, QStandardItem
from notesapp.notebooks import Notebooks
from notesapp.ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.init_notebooks_vm()
        self.populate_notebooks()
    
    def init_notebooks_vm(self):
        self._notebooks_vm = QStandardItemModel()
        self._notebooks_vm.setColumnCount(1)
        self.listView_notebooks.setModel(self._notebooks_vm)
    
        self._root_item = self._notebooks_vm.invisibleRootItem()

    def populate_notebooks(self):
        nbs = Notebooks()
        notebooks = nbs.get_notebooks()

        for idx, nb in enumerate(notebooks):
            item = QStandardItem(nb['title'])
            item.setData(nb['id'], QtCore.Qt.UserRole + 1)
            self._root_item.appendRow(item)



