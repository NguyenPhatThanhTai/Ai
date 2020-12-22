import os
import sys
import webbrowser

import playsound
import speech_recognition
import speech_recognition as sr
from cgitb import text
from datetime import date, datetime
from gtts import gTTS
from wikipedia import wikipedia
from IPython.external.qt_for_kernel import QtCore
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
counter = 0


class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)
    AiResult = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def task(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        print("Say something!")
        with m as source:
            ai_brain = ""
            audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                value = r.recognize_google(audio, language='vi-VN')
                self.textChanged.emit(value)
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
                elif value == "dừng lại":
                    ai_brain = "Chào tạm biệt và hẹn gặp lại, bye bye!!!"
                    self.AiResult.emit(ai_brain)
                    speak(ai_brain)
                    exit()
                elif "tắt máy" in value:
                    ai_brain = "Ok bạn muốn tôi tắt máy trong bao lâu nữa: bây giờ, 5 phút nữa, 10 phút nữa, 15 phút nữa, 30 phút nữa hay 1 giờ nữa"
                    self.AiResult.emit(ai_brain)
                    speak(ai_brain)
                    audio = r.listen(source)
                    value = r.recognize_google(audio, language='vi-VN')
                    if value == "bây giờ":
                        ai_brain = "ok tôi sẽ tắt máy giúp bạn ngay bây giờ"
                        os.system('shutdown -s -t 0')
                    elif value == "5 phút nữa":
                        os.system('shutdown -s -t 300')
                        ai_brain = "ok tôi sẽ tắt máy giúp bạn sau 5 phút"
                    elif value == "10 phút nữa":
                        os.system('shutdown -s -t 600')
                        ai_brain = "ok tôi sẽ tắt máy giúp bạn sau 10 phút"
                    elif value == "15 phút nữa":
                        os.system('shutdown -s -t 900')
                        ai_brain = "ok tôi sẽ tắt máy giúp bạn sau 15 phút"
                    elif value == "30 phút nữa":
                        os.system('shutdown -s -t 1800')
                        ai_brain = "ok tôi sẽ tắt máy giúp bạn sau 30 phút"
                    elif value == "1 giờ nữa":
                        os.system('shutdown -s -t 3600')
                        ai_brain = "ok tôi sẽ tắt máy giúp bạn sau 1 giờ nữa"
                    else:
                        ai_brain = "Thời gian không hợp lệ"

                    self.textChanged.emit(value)
                    self.AiResult.emit(ai_brain)
                elif "khởi động lại" or "restart" in value:
                    ai_brain = "ok tôi sẽ giúp bạn khởi động lại máy ngay bây giờ"
                    self.AiResult.emit(ai_brain)
                    speak(ai_brain)
                    os.system('shutdown -r -t 0')
                elif "Google" in value:
                    ai_brain = "Ok bạn muốn tôi tìm gì trên google nào"
                    self.AiResult.emit(ai_brain)
                    speak(ai_brain)
                    audio = r.listen(source)
                    value = r.recognize_google(audio, language='vi-VN')
                    url = 'https://google.com/search?q=' + value
                    self.textChanged.emit(value)
                    webbrowser.get().open(url)
                    ai_brain = "Đây là những gì tôi có thể tìm cho bạn"
                    print("You said: {}".format(text))
                elif "Wikipedia" in value:
                    ai_brain = "Ok bạn muốn tôi tìm gì trên wikipedia nào"
                    self.AiResult.emit(ai_brain)
                    speak(ai_brain)
                    audio = r.listen(source)
                    value = r.recognize_google(audio, language='vi-VN')
                    self.textChanged.emit(value)
                    try:
                        wikipedia.set_lang("vi")
                        ai_brain = wikipedia.summary(value, sentences=1)
                    except wikipedia.exceptions.PageError as e:
                        ai_brain = "Thông tin này tạm thời tôi chưa tìm được, mong bạn thông cảm"
                else:
                    ai_brain = "Thông tin này tạm thời tôi chưa tìm được, mong bạn thông cảm"
                    print("AI: " + ai_brain)

                self.AiResult.emit(ai_brain)
                speak(ai_brain)

            except sr.UnknownValueError:
                print("Oops")


def speak(ai_brain):
    tts = gTTS(text=ai_brain, lang='vi')
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

        self.button = self.findChild(QtWidgets.QPushButton, 'pb_Start')
        self.button.clicked.connect(self.worker.task)
        self.button2 = self.findChild(QtWidgets.QPushButton, 'pb_Exit')
        self.button2.clicked.connect(QCoreApplication.instance().quit)

        self.label = self.findChild(QtWidgets.QLabel, 'lb_user')
        self.worker.textChanged.connect(self.label.setText)
        self.label2 = self.findChild(QtWidgets.QLabel, 'lb_Ai')
        self.worker.AiResult.connect(self.label2.setText)

        self.show()


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(SplashScreen, self).__init__()
        uic.loadUi('splash_screen.ui', self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(255, 255, 255, 0))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        QtCore.QTimer.singleShot(2500, lambda: self.label_description.setText("<strong>KHỞI TẠO CƠ SỞ DỮ LIỆU"))
        QtCore.QTimer.singleShot(4200, lambda: self.label_description.setText("<strong>GẦN XONG CHỜ MỘT CHÚT NHÉ"))
        self.show()

    def progress(self):
        global counter
        self.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1


app = QtWidgets.QApplication(sys.argv)
windows = SplashScreen()
sys.exit(app.exec_())
