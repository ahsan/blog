import numpy as np
import matplotlib.pyplot as plt

freq = 1
w = 2 * np.pi * freq
symbol_phase_angles = [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]

time_granularity = 1/100
time = np.arange(0, len(symbol_phase_angles), time_granularity)
signal = np.zeros(len(time))

for phase_ind, phase in enumerate(symbol_phase_angles):
    start = int(phase_ind/time_granularity)+1
    end = int((phase_ind + 1)/time_granularity)
    time_slice = time[start:end]
    signal[start:end] = np.sin(np.multiply(time_slice, w) + phase) + \
        np.cos(np.multiply(time_slice, w) + phase)

plt.plot(time, signal)

plt.title('QPSK("11 01 00 10")')
plt.xlabel('Time ->')
plt.ylabel('Amplitude')

plt.yticks(np.array([]))
plt.xticks([i + freq/2 for i in range(len(symbol_phase_angles))],
           ['11', '01', '00', '10'])

plt.axhline(y=0, color='k')
plt.show()
