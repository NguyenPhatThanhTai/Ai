import sys
from cgitb import text

from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
from PyQt5.QtCore import QCoreApplication
from gtts import gTTS
import wikipedia
import playsound
import os
from datetime import date, datetime
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

    # def getUserSpeak():
    #     # khởi tạo
    #     ai_brain = " "  # Ban đầu nó chưa được học gì cả nên cũng chưa có thông tin
    #     ai_ear = speech_recognition.Recognizer()  # nghe người dùng nói
    #
    #     with speech_recognition.Microphone() as mic:
    #         print("AI: Đang nghe ( 5 giây )")
    #         audio = ai_ear.record(mic, duration=5)
    #         # AI nghe trong vòng 5 giây rồi tắt mic
    #         print("AI: ... ")
    #     try:
    #         you = ai_ear.recognize_google(audio, language='vi-VN')
    #         # nghe và nói giọng việt nam
    #         print("Bạn:  " + you)
    #
    #     except:
    #         ai_brain = "Tôi không hiểu bạn nói gì cả ! ..."
    #         speak(ai_brain)
    #         print("AI:  " + ai_brain)
    #     return you
    #
    # def runAi(you):
    #         if "Xin chào" in you:
    #             ai_brain = "Xin chào Bạn."
    #         elif "thời tiết" in you:
    #             ai_brain = "Tôi là máy móc nên chưa biết thời tiết nha."
    #         elif "ngày" in you:
    #             today = date.today()
    #             ai_brain = today.strftime("%d/%m/%Y")
    #         elif "giờ" in you:
    #             now = datetime.now()
    #             ai_brain = now.strftime("%H:%M:%S")
    #         elif you:
    #             try:
    #                 wikipedia.set_lang("vi")
    #                 ai_brain = wikipedia.summary(you, sentences=1)
    #             except wikipedia.exceptions.PageError as e:
    #                 ai_brain = "Thông tin này tạm thời tôi chưa tìm được, mong bạn thông cảm"
    #         elif "Dừng lại" in you:
    #             ai_brain = "Chào tạm biệt và hẹn gặp lại."
    #             print("AI: " + ai_brain)
    #             speak(ai_brain)
    #             exit()
    #         else:
    #             ai_brain = "Thông tin này tạm thời tôi chưa tìm được, mong bạn thông cảm"
    #             print("AI: " + ai_brain)
    #
    #         speak(ai_brain)
    #         return ai_brain
def Gui():
    app = QtWidgets.QApplication(sys.argv)

    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    window = QtWidgets.QWidget()
    window.setGeometry(200, 500, 400, 500)
    window.setWindowTitle("Hãy hỏi nó :v")

    title_label = QtWidgets.QLabel(window)
    title_label.setText("Hãy hỏi nó :v")
    title_label.move(135,10)
    title_label.resize(200, 50)
    title_label.setFont(QtGui.QFont("SansSerif", 15))

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("Chương trình đã chạy")
    programs_says.resize(200, 50)
    programs_says.move(24,100)

    you_says = QtWidgets.QLabel(window)
    you_says.move(25,100)


    you_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(you_text.setText)
    you_text.move(25,120)
    you_text.resize(20000,50)

    you_text = QtWidgets.QLabel(window)
    worker.AiResult.connect(you_text.setText)
    you_text.setWordWrap(True)
    you_text.move(25,150)
    you_text.resize(300,300)

    start_button = QtWidgets.QPushButton("Bắt đầu hỏi")
    close_button = QtWidgets.QPushButton("Kết thúc nào")


    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(start_button)
    v_box.addWidget(close_button)
    window.setLayout(v_box)

    start_button.clicked.connect(worker.task)
    close_button.clicked.connect(QCoreApplication.instance().quit)
    window.show()
    sys.exit(app.exec())


Gui()