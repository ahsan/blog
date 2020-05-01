import numpy as np
import matplotlib.pyplot as plt

f_carrier = 10
w_carrier = 2 * np.pi * f_carrier
f_input = 1
w_input = 2 * np.pi * f_input


time_granularity = 1/300
time = np.arange(0, 1, time_granularity)
input_signal = np.sin(np.multiply(time, w_input))

am_output_signal = np.multiply(
    np.sin(np.multiply(time, w_carrier)), input_signal)

fm_output_signal = np.zeros_like(time)
for i, t in enumerate(time):
    fm_output_signal[i] = np.sin(
        2. * np.pi * (f_carrier * t + input_signal[i]))

plt.subplot(1, 2, 1)
plt.plot(time, input_signal)
plt.plot(time, am_output_signal)
plt.title('Amplitude Modulation')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(1, 2, 2)
plt.plot(time, input_signal)
plt.plot(time, fm_output_signal)
plt.title('Frequency Modulation')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.show()
