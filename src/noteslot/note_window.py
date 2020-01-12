"""
MainWindow module
author: Julien Dcruz
"""

import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Signal, Slot, QSize, QPoint, QEvent, QTimer
from PySide2.QtWidgets import QWidget, QApplication, QTableView, QFileDialog
from noteslot.ui.ui_notewindow import Ui_NoteWindow
from noteslot.notes import Notes
from noteslot import noteslot_rc


class NoteWindow(QWidget, Ui_NoteWindow):

    closed = QtCore.Signal(int)
    show_main = QtCore.Signal()
    hide_main = QtCore.Signal()

    def __init__(self, note_id, parent=None):
        super(NoteWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

        self.textEdit_note.setAcceptRichText(True)

        self.load_note(note_id)

        self.textEdit_note.textChanged.connect(self.text_changed)
        self.btn_showmain.clicked.connect(self.show_main)
        self.btn_hide.clicked.connect(self.hide_note)

        if self._note['width'] is not None:
            self.resize(QSize(self._note['width'], self._note['height']))
        if self._note['pos_x'] is not None:
            self.move(QPoint(self._note['pos_x'], self._note['pos_y']))

        self._nts.saveStatus(self._note['id'], True)

        self._save_timer = QTimer()
        self._save_timer.setSingleShot(True)
        self._save_timer.timeout.connect(self.save_content)

        self._last_w = None
        self._last_h = None
        self._last_x = None
        self._last_y = None

    def load_note(self, note_id):
        self._nts = Notes()
        self._note = self._nts.get(note_id)

        self.setWindowTitle(self._note['title'])
        self.textEdit_note.setText(self._note['content'])

    @Slot()
    def text_changed(self):
        if not self._save_timer.isActive():
            self._save_timer.start(5000)

    @Slot()
    def save_content(self):
        content = self.textEdit_note.toHtml()
        self._nts.update(self._note['id'],
                         self._note['title'], content, True)

    @Slot()
    def hide_note(self, event):
        self._nts.saveStatus(self._note['id'], False)
        self.close()

    def closeEvent(self, event):
        self.save_content()
        self._nts.saveSize(self._note['id'], self.width(), self.height())
        self._nts.savePos(
            self._note['id'], self.pos().x(), self.pos().y())
