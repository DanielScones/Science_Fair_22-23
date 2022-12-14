#https://fazals.ddns.net/spectrum-analyser-part-1/

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


    toggle = 0
    

    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    line.set_ydata(dataInt)
    
    for i in range(len(dataInt)):
        InverseY[i] = -dataInt[i]
    line2.set_ydata(InverseY)

    if keyboard.is_pressed("space") == 1 and toggle == 0:
        toggle = 1
        while toggle == 1:

            space = keyboard.is_pressed("space")

            line.set_ydata(dataInt)
            line2.set_ydata(InverseY)

            fig.canvas.draw()
            fig.canvas.flush_events()
            print(toggle)
            if keyboard.is_pressed("space") == 0:
                toggle = 0
                while toggle == 0:
                    space = keyboard.is_pressed("space")

                    line.set_ydata(dataInt)
                    line2.set_ydata(InverseY)

                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    if space == 1:
                        break

    print(toggle)
    fig.canvas.draw()
    fig.canvas.flush_events()
    

    
    


#          & "l:/Python/Science Fair 2022/env/Scripts/python.exe" "l:/Python/Science Fair 2022/MightWork.PY"