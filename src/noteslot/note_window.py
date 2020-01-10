"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Signal, Slot, QSize, QPoint, QEvent
from PySide2.QtWidgets import QWidget, QApplication, QTableView, QFileDialog
from noteslot.ui.ui_notewindow import Ui_NoteWindow
from noteslot.notes import Notes
from noteslot import noteslot_rc


class NoteWindow(QWidget, Ui_NoteWindow):

    closed = QtCore.Signal(int)

    def __init__(self, note_id, parent=None):
        super(NoteWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Tool)

        self.textEdit_note.setAcceptRichText(True)

        self.load_note(note_id)

        self.textEdit_note.textChanged.connect(self.text_changed)
        self.btn_hide.clicked.connect(self.hide_note)

        if self._note['width'] is not None:
            self.resize(QSize(self._note['width'], self._note['height']))
        if self._note['pos_x'] is not None:
            self.move(QPoint(self._note['pos_x'], self._note['pos_y']))

        print(self._note['id'])
        self._nts.updateStatus(self._note['id'], True)

    def closeEvent(self, event):
        self._nts.updateStatus(self._note['id'], False)
        self.closed.emit(self._note['id'])

    def resizeEvent(self, event):
        self._nts.updateSize(
            self._note['id'], event.size().width(), event.size().height())

    def moveEvent(self, event):
        self._nts.updatePos(
            self._note['id'], event.pos().x(), event.pos().y())

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

    @Slot()
    def hide_note(self, event):
        self._nts.updateStatus(self._note['id'], False)
        self.close()
