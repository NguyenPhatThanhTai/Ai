# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MaingDzWbC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(529, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Tittler = QLabel(self.centralwidget)
        self.Tittler.setObjectName(u"Tittler")
        self.Tittler.setGeometry(QRect(190, 20, 151, 31))
        font = QFont()
        font.setFamily(u"OCR A Extended")
        font.setPointSize(12)
        self.Tittler.setFont(font)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 70, 441, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 439, 439))
        self.Ai = QLabel(self.scrollAreaWidgetContents)
        self.Ai.setObjectName(u"Ai")
        self.Ai.setGeometry(QRect(10, 100, 421, 321))
        self.Ai.setTextFormat(Qt.PlainText)
        self.Ai.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Ai.setWordWrap(True)
        self.User = QLabel(self.scrollAreaWidgetContents)
        self.User.setObjectName(u"User")
        self.User.setEnabled(True)
        self.User.setGeometry(QRect(10, 10, 421, 61))
        self.User.setAutoFillBackground(False)
        self.User.setTextFormat(Qt.PlainText)
        self.User.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.User.setWordWrap(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 520, 161, 28))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 520, 171, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Tittler.setText(QCoreApplication.translate("MainWindow", u"Xin ch\u00e0o b\u1ea1n", None))
        self.Ai.setText(QCoreApplication.translate("MainWindow", u"Ai: ", None))
        self.User.setText(QCoreApplication.translate("MainWindow", u"Ng\u01b0\u1eddi d\u00f9ng: ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u tr\u00f2 chuy\u1ec7n", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
    # retranslateUi

