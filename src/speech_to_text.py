import whisper
import numpy as np
import pyaudio
from pyaudio import PyAudio
import os
import librosa
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"
CHUNK=1024 # No. of audio frames reader reads at once
FORMAT=pyaudio.paInt16 # A format of  16-bit integers (standard for recodordings)
CHANNELS=1 # This refers to audio channels (1 for mono) (2 for stereo), whisper expects mono audio so we choose 1 
RATE=44100 # its the sampling rate, standard quality
RECORD_SECONDS=5 # no. of seconds recordings

def record_audio(frames):
    p=PyAudio()
    stream=p.open(
        channels=CHANNELS,
        format=FORMAT,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
        )

    print("Recording...")

    for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
        data=stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate
    return frames



def normalize_audio(frames):
    # After recording:
    audio_bytes = b''.join(frames)
    # Convert bytes to numpy array of int16 samples
    audio_np = np.frombuffer(audio_bytes, dtype=np.int16)
    # Normalize to float32 in range [-1.0, 1.0]
    audio_float32 = audio_np.astype(np.float32) / 32768.0
    # Resample to 16000 Hz using librosa (or scipy)
    audio_resampled = librosa.resample(audio_float32, orig_sr=RATE, target_sr=16000)
    return audio_resampled


def transcribe_audio(model_name,audio_resampled):
    model=whisper.load_model(model_name)
    result=model.transcribe(audio_resampled)
    return result["text"]




    
