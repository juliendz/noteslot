# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_NoteWindow(object):
    def setupUi(self, NoteWindow):
        if NoteWindow.objectName():
            NoteWindow.setObjectName(u"NoteWindow")
        NoteWindow.resize(400, 300)
        self.verticalLayout = QVBoxLayout(NoteWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit_note = QTextEdit(NoteWindow)
        self.textEdit_note.setObjectName(u"textEdit_note")
        self.textEdit_note.setStyleSheet(u"background-color: rgb(255, 255, 136);")

        self.verticalLayout.addWidget(self.textEdit_note)


        self.retranslateUi(NoteWindow)

        QMetaObject.connectSlotsByName(NoteWindow)
    # setupUi

    def retranslateUi(self, NoteWindow):
        NoteWindow.setWindowTitle(QCoreApplication.translate("NoteWindow", u"Form", None))
    # retranslateUi

