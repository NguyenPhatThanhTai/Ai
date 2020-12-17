import os
import sys
import threading
from cgitb import text
from datetime import date, datetime
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, uic
from PyQt5.QtCore import QCoreApplication
from PySide2.QtWidgets import *
import speech_recognition as sr
from gtts import gTTS
import playsound
from wikipedia import wikipedia
from PyQt5 import QtWidgets, uic

from ui_Main import Ui_MainWindow


class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)
    AiResult = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def task(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        print("Say somethig!")
        with m as source:
            ai_brain = ""
            audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                value = r.recognize_google(audio, language='vi-VN')
                self.textChanged.emit("Bạn vừa nói là: " + value)
                print("You said: {}".format(text))
                if "Xin chào" in value:
                    ai_brain = "Xin chào Bạn."
                elif "thời tiết" in value:
                    ai_brain = "Tôi là máy móc nên chưa biết thời tiết nha."
                elif "ngày" in value:
                    today = date.today()
                    ai_brain = today.strftime("%d/%m/%Y")
                elif "giờ" in value:
                    now = datetime.now()
                    ai_brain = now.strftime("%H:%M:%S")
                elif value:
                    try:
                        wikipedia.set_lang("vi")
                        ai_brain = wikipedia.summary(value, sentences=1)
                    except wikipedia.exceptions.PageError as e:
                        ai_brain = "Thông tin này tạm thời tôi chưa tìm được, mong bạn thông cảm"
                elif "Dừng lại" in value:
                    ai_brain = "Chào tạm biệt và hẹn gặp lại."
                    print("AI: " + ai_brain)
                    speak(ai_brain)
                    exit()
                else:
                    ai_brain = "Thông tin này tạm thời tôi chưa tìm được, mong bạn thông cảm"
                    print("AI: " + ai_brain)

                self.AiResult.emit("-Ai nói là-: " + ai_brain + "...")
                speak(ai_brain)

            except sr.UnknownValueError:
                print("Oops")

def speak(ai_brain):
    tts = gTTS(text = ai_brain, lang = 'vi')
    tts.save("D:\\ai.mp3")
    playsound.playsound("D:\\ai.mp3")
    os.remove("D:\\ai.mp3")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Main.ui', self)

        self.worker = VoiceWorker()
        self.thread = QtCore.QThread()
        self.thread.start()
        self.worker.moveToThread(self.thread)


        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button.clicked.connect(self.worker.task)
        self.button2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.button2.clicked.connect(QCoreApplication.instance().quit)

        self.label = self.findChild(QtWidgets.QLabel, 'User')
        self.worker.textChanged.connect(self.label.setText)
        self.label2 = self.findChild(QtWidgets.QLabel, 'Ai')
        self.worker.AiResult.connect(self.label2.setText)

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindow()
    sys.exit(app.exec_())
