#https://fazals.ddns.net/spectrum-analyser-part-1/

from pickle import FALSE
import time
import numpy as np 
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt
import keyboard

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # in Hz



p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

toggle = 0

fig,ax = plt.subplots()
x = np.arange(0,2*CHUNK,2)
InverseY = np.arange(0,2*CHUNK,2)
line, = ax.plot(x, np.random.rand(CHUNK),'r')
line2, = ax.plot(x, np.random.rand(CHUNK),'r', color = 'blue')
ax.set_ylim(-32000,32000)
ax.ser_xlim = (0,CHUNK)
fig.show()

fig.canvas.draw()
fig.canvas.flush_events()
fig.text(.5, .0001, "press space to pause", ha='center')

while True:

    keys = keyboard.is_pressed('z'), keyboard.is_pressed('x')
    pause_play = True

    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    line.set_ydata(dataInt)
    
    for i in range(len(dataInt)):
        InverseY[i] = -dataInt[i]
    line2.set_ydata(InverseY)

    
    if keys[1] == 1:
        pause_play = False
    
    while pause_play == False:
        keys = keyboard.is_pressed('z'), keyboard.is_pressed('x')
        if keys[0] == 1:
            pause_play = True
        line.set_ydata(dataInt)
        line2.set_ydata(InverseY)
        fig.canvas.draw()
        fig.canvas.flush_events()
    

    print(toggle)
    fig.canvas.draw()
    fig.canvas.flush_events()
    

    
    


#          & "l:/Python/Science Fair 2022/env/Scripts/python.exe" "l:/Python/Science Fair 2022/MightWork.PY"