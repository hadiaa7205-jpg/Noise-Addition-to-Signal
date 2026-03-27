Project 2: Noise Addition to Signal
Purpose: To demonstrate effect of noise on a signal

import numpy as np
import matplotlib.pyplot as plt

Time vector
t = np.linspace(0, 1, 1000)

Original signal (sine wave)
frequency = 5
original_signal = np.sin(2 * np.pi * frequency * t)

Generate noise
noise = 0.5 * np.random.randn(len(t))

Add noise to signal
noisy_signal = original_signal + noise

Plotting
plt.figure(figsize=(10,5))

plt.subplot(2,1,1)
plt.plot(t, original_signal)
plt.title("Original Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(2,1,2)
plt.plot(t, noisy_signal)
plt.title("Noisy Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
