# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainKGCzom.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Picture import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 665)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, -10, 1191, 681))
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lb_user = QLabel(self.groupBox)
        self.lb_user.setObjectName(u"lb_user")
        self.lb_user.setGeometry(QRect(180, 90, 321, 111))
        font = QFont()
        font.setPointSize(10)
        self.lb_user.setFont(font)
        self.lb_user.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lb_user.setWordWrap(True)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 70, 441, 201))
        self.label.setPixmap(QPixmap(u":/newPrefix/C:/Users/THANH TAI/OneDrive/Pictures/speech-29435_1280.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 310, 291, 281))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/man.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 300, 331, 291))
        self.label_3.setPixmap(QPixmap(u":/newPrefix/7904424933cc535b666f2de669973530.gif"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(720, 100, 441, 201))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/C:/Users/THANH TAI/OneDrive/Pictures/speech-29435_1280.png"))
        self.label_4.setScaledContents(True)
        self.lb_Ai = QLabel(self.groupBox)
        self.lb_Ai.setObjectName(u"lb_Ai")
        self.lb_Ai.setGeometry(QRect(790, 120, 321, 111))
        self.lb_Ai.setFont(font)
        self.lb_Ai.setScaledContents(False)
        self.lb_Ai.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lb_Ai.setWordWrap(True)
        self.pb_Start = QPushButton(self.groupBox)
        self.pb_Start.setObjectName(u"pb_Start")
        self.pb_Start.setGeometry(QRect(370, 550, 141, 61))
        self.pb_Start.setStyleSheet(u"image: url(:/newPrefix/on-button.png);\n"
"background-color: rgb(60, 87, 87);\n"
"")
        self.pb_Start.setAutoDefault(False)
        self.pb_Start.setFlat(True)
        self.pb_Exit = QPushButton(self.groupBox)
        self.pb_Exit.setObjectName(u"pb_Exit")
        self.pb_Exit.setGeometry(QRect(540, 550, 131, 61))
        self.pb_Exit.setStyleSheet(u"image: url(:/newPrefix/exit.png);\n"
"background-color: rgb(255, 123, 121);")
        self.pb_Exit.setAutoDefault(False)
        self.pb_Exit.setFlat(True)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(420, 620, 61, 21))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(590, 620, 61, 21))
        self.label.raise_()
        self.lb_user.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lb_Ai.raise_()
        self.pb_Start.raise_()
        self.pb_Exit.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pb_Start.setDefault(False)
        self.pb_Exit.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.lb_user.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.lb_Ai.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pb_Start.setText("")
        self.pb_Exit.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
    # retranslateUi

