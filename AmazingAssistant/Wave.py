import os
import struct
import sys

import pylab
from numpy.lib import stride_tricks
from scipy.fftpack import fft
from scipy.io import wavfile
import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy import signal as sgn
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
# r = sr.Recognizer()
# m = sr.Microphone()
# with m as source:
#     audio = r.listen(source)
#     value = r.recognize_google(audio, language="vi-VN")
#     tts = gTTS(text=value, lang="vi")
#     tts.save("test.mp3")
#     sound = AudioSegment.from_mp3('test.mp3')
#     sound.export('test.wav', format="wav")

#sampling(lấy mẫu các chiều cao của sóng âm)
spf = wave.open("record.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
fs = spf.getframerate()


Time = np.linspace(0, len(signal) / fs, num=len(signal))

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(Time, signal)
plt.show()

b = [0]
for i in signal:
    b.append(i)
print(b)


########################
def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('spectrogram.png')
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

graph_spectrogram('record.wav')

