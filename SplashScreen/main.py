import sys
import threading
from concurrent.futures import thread

import speech_recognition
from gtts import gTTS
import wikipedia
import playsound
import os
from datetime import date, datetime

from PySide2 import QtGui, QtWidgets
from PySide2 import QtCore
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_SplashScreen
from ui_main import Ui_MainWindow, QCoreApplication
from Controller import VoiceWorker
# from Controller import runAi
# from  Controller import speak
# from Controller import getUserSpeak

def on_clicked():
    th = threading.Thread(target=(VoiceWorker()))
    th.daemon = True
    th.start()

# Giao dien chinh
class MainWindow(QMainWindow, QtWidgets.QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.click.connect(on_clicked())

# Giao dien loading
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main = MainWindow()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(255, 255, 255, 0))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.ui.label_description.setText("CHÀO MỪNG ĐẾN VỚI BẢN THỬ NGHIỆM")
        QtCore.QTimer.singleShot(2500, lambda: self.ui.label_description.setText("KHỞI TẠO CƠ SỞ DỮ LIỆU"))
        QtCore.QTimer.singleShot(4200, lambda: self.ui.label_description.setText("GẦN XONG CHỜ MỘT CHÚT NHÉ"))
        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main.show()
            self.close()
        counter += 1


if __name__ == "__main__":
    app = QApplication()
    windows = SplashScreen()
    sys.exit(app.exec_())




