import numpy as np
import matplotlib.pyplot as plt

freq = 10
time = .2
samples = 5000 #smoothness
Ts = 1./samples
N = int(time/Ts)# num of intervals

t = np.linspace(0, time, N)# evenly spaced numbers
signal2 = np.sin(2*np.pi*freq*t)
signal = np.sin(-(2*np.pi*freq*t))
a = signal + signal2

plt.plot(t, signal)
plt.plot(t, signal2)
plt.plot(t, a)
plt.show()