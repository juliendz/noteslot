# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1188, 725)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_searchicon = QLabel(self.frame)
        self.label_searchicon.setObjectName(u"label_searchicon")
        self.label_searchicon.setGeometry(QRect(10, 10, 31, 30))
        self.label_searchicon.setMaximumSize(QSize(128, 16777215))
        self.label_searchicon.setPixmap(QPixmap(u":/icons/resources/icons/search.png"))
        self.label_searchicon.setScaledContents(True)
        self.label_search = QLabel(self.frame)
        self.label_search.setObjectName(u"label_search")
        self.label_search.setGeometry(QRect(50, 20, 37, 16))
        self.label_search.setTextFormat(Qt.AutoText)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(99, 10, 1061, 30))

        self.verticalLayout.addWidget(self.frame)

        self.frame_notes = QFrame(self.centralwidget)
        self.frame_notes.setObjectName(u"frame_notes")
        self.frame_notes.setFrameShape(QFrame.StyledPanel)
        self.frame_notes.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_notes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.frame_notes)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_notes)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1188, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_searchicon.setText("")
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"Search:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

