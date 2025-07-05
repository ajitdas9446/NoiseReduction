# DSP Voice Noise Reduction Mini-Project

## Overview
This project demonstrates Digital Signal Processing (DSP) noise reduction** on voice signals using spectral subtraction in Python. Users can record a 20-second noisy voice sample or use a provided example audio file, then apply noise reduction to generate a cleaner speech output.

## Features
- Record or use example noisy audio.
- Apply spectral subtraction for noise reduction.
- Save cleaned output for listening and testing.
- Plot waveforms before and after noise reduction.

## Files
- voice_noise_reduction.py – Main script.
- noisy_voice.wav – voice you will select or record noisy audio.
- cleaned_voice.wav – Output after cleaning.
- example_noisy_voise.wav -example noisy voice
- README.md – This file.

## How to Run
1. Install dependencies:
```bash
pip install numpy scipy matplotlib sounddevice noisereduce
```
2. Run:
```bash
python3 noiseReduction.py
```
3. Choose to record or use the example file and press enter, then the cleaned output will be saved as cleaned_voice.wav and plots will be generated.


## Author
Ajit Das 
B.E. Computer Engineering  
Kathmandu University