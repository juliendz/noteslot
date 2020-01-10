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
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(NoteWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 235, 129);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_hide = QPushButton(self.frame)
        self.btn_hide.setObjectName(u"btn_hide")

        self.horizontalLayout.addWidget(self.btn_hide)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(NoteWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit_note = QTextEdit(self.frame_2)
        self.textEdit_note.setObjectName(u"textEdit_note")
        self.textEdit_note.setStyleSheet(u"background-color: rgb(255, 255, 136);")

        self.horizontalLayout_2.addWidget(self.textEdit_note)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(NoteWindow)

        QMetaObject.connectSlotsByName(NoteWindow)
    # setupUi

    def retranslateUi(self, NoteWindow):
        NoteWindow.setWindowTitle(QCoreApplication.translate("NoteWindow", u"Form", None))
        self.btn_hide.setText(QCoreApplication.translate("NoteWindow", u"Hide", None))
    # retranslateUi

