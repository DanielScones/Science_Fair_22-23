import numpy as np
from scipy.io import wavfile

fs = 44100

f = int(input("Enter fundamental frequency: "))
t = float(input("Enter duration of signal (in seconds): "))

samples = np.arange(-10, 10, 0.1)

signal = np.sin(2 * np.pi * f * samples)

signal *= 32767

signal = np.int16(signal)

wavfile.write(str(input("Name your audio: ")), fs, signal)