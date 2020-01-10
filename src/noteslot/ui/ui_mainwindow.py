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
        MainWindow.resize(500, 500)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_newnotebook = QAction(MainWindow)
        self.action_newnotebook.setObjectName(u"action_newnotebook")
        self.action_checkupdates = QAction(MainWindow)
        self.action_checkupdates.setObjectName(u"action_checkupdates")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_search = QLabel(self.frame)
        self.label_search.setObjectName(u"label_search")
        self.label_search.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label_search)

        self.plainTextEdit_search = QPlainTextEdit(self.frame)
        self.plainTextEdit_search.setObjectName(u"plainTextEdit_search")

        self.horizontalLayout.addWidget(self.plainTextEdit_search)

        self.btn_clearsearch = QPushButton(self.frame)
        self.btn_clearsearch.setObjectName(u"btn_clearsearch")
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clearsearch.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_clearsearch)


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
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_newnotebook)
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_checkupdates)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_newnotebook.setText(QCoreApplication.translate("MainWindow", u"New Notebook", None))
        self.action_checkupdates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates", None))
        self.label_search.setText(QCoreApplication.translate("MainWindow", u"Search:", None))
        self.btn_clearsearch.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

