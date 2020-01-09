"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QWidget, QApplication, QTableView, QFileDialog
from notesapp.ui.ui_notewindow import Ui_NoteWindow
from notesapp.notes import Notes
from notesapp import notesapp_rc


class NoteWindow(QWidget, Ui_NoteWindow):

    closed = QtCore.Signal(int)

    def __init__(self, note_id, parent=None):
        super(NoteWindow, self).__init__(parent)
        self.setupUi(self)
        self.textEdit_note.setAcceptRichText(True)

        self.load_note(note_id)

        self.textEdit_note.textChanged.connect(self.text_changed)

    def closeEvent(self, event):
        self.closed.emit(self._note['id'])

    def load_note(self, note_id):
        self._nts = Notes()
        self._note = self._nts.get(note_id)

        self.setWindowTitle(self._note['title'])
        self.textEdit_note.setText(self._note['content'])

    @Slot()
    def text_changed(self):
        # TODO: This is called everytime keyup occurs which means db is being updated every keypress, may need to optimize
        content = self.textEdit_note.toHtml()
        self._nts.update(self._note['id'],
                         self._note['title'], content, True)
