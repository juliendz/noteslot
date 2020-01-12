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
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/notebook.png", QSize(), QIcon.Normal, QIcon.Off)
        NoteWindow.setWindowIcon(icon)
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

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_showmain = QPushButton(self.frame_3)
        self.btn_showmain.setObjectName(u"btn_showmain")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_showmain.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_showmain)

        self.btn_hide = QPushButton(self.frame_3)
        self.btn_hide.setObjectName(u"btn_hide")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_hide.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btn_hide)


        self.horizontalLayout.addWidget(self.frame_3)


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
        self.btn_showmain.setText("")
        self.btn_hide.setText("")
    # retranslateUi

