import numpy as np
import scipy.io.wavfile as wav
import os

AUDIO_DIR = 'videos/01_is-ai-a-bubble-ask-the-railways/audio_takes'
os.makedirs(AUDIO_DIR, exist_ok=True)
SAMPLE_RATE = 44100
DURATION = 380  # ~6.3 minutes

def generate_cinematic_drone():
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
    
    # Deep cinematic D-minor chord fundamentals & harmonics
    # D1 = 36.71 Hz, A1 = 55.0 Hz, D2 = 73.42 Hz, F2 = 87.31 Hz, A2 = 110.0 Hz, C3 = 130.81 Hz
    f_sub = 36.71
    f_root = 73.42
    f_fifth = 110.0
    f_third = 87.31
    f_seven = 130.81
    
    # Slow LFOs for organic tape-like movement (0.05 Hz to 0.15 Hz)
    lfo1 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.08 * t)
    lfo2 = 0.5 + 0.5 * np.cos(2 * np.pi * 0.05 * t)
    lfo3 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.12 * t)
    
    # Sub bass layer
    sub = 0.35 * np.sin(2 * np.pi * f_sub * t)
    # Warm octave root with subtle detune (chorus effect)
    root_l = 0.25 * np.sin(2 * np.pi * (f_root - 0.2) * t) * lfo1
    root_r = 0.25 * np.sin(2 * np.pi * (f_root + 0.2) * t) * lfo2
    # Fifth
    fifth = 0.18 * np.sin(2 * np.pi * f_fifth * t) * lfo2
    # Minor third (dark emotional tension)
    third = 0.15 * np.sin(2 * np.pi * f_third * t) * lfo3
    # Subtle 7th shimmer
    seven = 0.08 * np.sin(2 * np.pi * f_seven * t) * lfo1
    
    # Pink noise texture (tape hiss / room air)
    noise = np.random.normal(0, 0.015, len(t))
    # Simple moving average lowpass for warm texture
    b = np.ones(50) / 50
    warm_noise = np.convolve(noise, b, mode='same')
    
    left = sub + root_l + fifth + third + seven + warm_noise
    right = sub + root_r + fifth + third + seven + warm_noise
    
    # Fade in (3s) and Fade out (5s)
    fade_in = np.clip(np.linspace(0, 1, int(SAMPLE_RATE * 3)), 0, 1)
    fade_out = np.clip(np.linspace(1, 0, int(SAMPLE_RATE * 5)), 0, 1)
    left[:len(fade_in)] *= fade_in
    right[:len(fade_in)] *= fade_in
    left[-len(fade_out):] *= fade_out
    right[-len(fade_out):] *= fade_out
    
    # Normalize to -16dB
    stereo = np.vstack([left, right]).T
    max_val = np.max(np.abs(stereo))
    if max_val > 0:
        stereo = (stereo / max_val) * 0.25
    
    out_path = os.path.join(AUDIO_DIR, 'ambient_drone.wav')
    wav.write(out_path, SAMPLE_RATE, (stereo * 32767).astype(np.int16))
    print(f"Generated {out_path} ({DURATION}s)")

def generate_transition_whoosh():
    dur = 0.8
    t = np.linspace(0, dur, int(SAMPLE_RATE * dur), endpoint=False)
    # Pitch sweep down from 220Hz to 60Hz
    freq = np.linspace(220, 60, len(t))
    phase = 2 * np.pi * np.cumsum(freq) / SAMPLE_RATE
    tone = 0.4 * np.sin(phase)
    # Bandpassed noise whoosh
    noise = np.random.normal(0, 0.3, len(t))
    env = np.sin(np.pi * t / dur) ** 2  # Bell envelope
    whoosh = (tone + noise) * env * 0.3
    stereo = np.vstack([whoosh, whoosh]).T
    out_path = os.path.join(AUDIO_DIR, 'transition_whoosh.wav')
    wav.write(out_path, SAMPLE_RATE, (stereo * 32767).astype(np.int16))
    print(f"Generated {out_path}")

generate_cinematic_drone()
generate_transition_whoosh()
print("Audio soundscape generation complete!")
