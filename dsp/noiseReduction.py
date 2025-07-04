# DSP Project: Record or Use Example File for Noise Reduction

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write, read
import noisereduce as nr
import os

fs = 16000  # Sampling frequency
print("Options:")
print("r: Record new audio")
print("e: Use example_noisy_voice.wav")
choice = input("Enter your choice (r/e): ").strip().lower()

if choice == 'r':
    duration = 20  # seconds
    print("Recording for 20 seconds with fan noise, please speak...")
    data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    write('noisy_voice.wav', fs, (data * 32767).astype(np.int16))
    print('Recording saved as noisy_voice.wav.')
elif choice == 'e':
    if not os.path.exists('example_noisy_voice.wav'):
        print('Error: example_noisy_voice.wav not found. Please place it in this folder.')
        exit()
    else:
        print('Using example_noisy_voice.wav for processing.')
        example_file = 'example_noisy_voice.wav'
        target_file = 'noisy_voice.wav'
        with open(example_file, 'rb') as src, open(target_file, 'wb') as dst:
            dst.write(src.read())
else:
    print("Invalid choice. Please enter 'r' or 'e'.")
    exit()

# Load and normalize
ds, data = read('noisy_voice.wav')
data = data[:, 0] if data.ndim > 1 else data
data = data / np.max(np.abs(data))

# ------------------------
# Noise reduction
# ------------------------
reduced_noise = nr.reduce_noise(y=data, sr=fs)
reduced_noise = reduced_noise / np.max(np.abs(reduced_noise))
write('cleaned_voice.wav', fs, (reduced_noise * 32767).astype(np.int16))
print('Denoised recording saved as cleaned_voice.wav.')

# ------------------------
# Plot for report
# ------------------------
t = np.arange(len(data)) / fs
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, data)
plt.title('Original Noisy Voice Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, reduced_noise)
plt.title('Denoised Voice Using NoiseReduce')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()