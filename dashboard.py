import streamlit as st
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import io


# Fungsi untuk plot waveform
def plot_waveform(audio_path, title):
    sound = AudioSegment.from_file(audio_path)
    samples = np.array(sound.get_array_of_samples())
    fig, ax = plt.subplots()
    ax.plot(samples, linewidth=0.5)
    ax.set_title(title)
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")
    st.pyplot(fig)

# Header
st.title("Audio Playback & Waveform Comparison")
st.markdown("**Perbandingan Audio Playback Normal, 0.75x, dan 1.5x**")

# Audio Normal
st.subheader("Original Audio")
st.audio("file_example_MP3_1MG.mp3")
plot_waveform("file_example_MP3_1MG.mp3", "Waveform - Original")

# Audio Slow
st.subheader("Slow Playback (0.75x)")
st.audio("file_example_MP3_1MG-slow.mp3")
plot_waveform("file_example_MP3_1MG-slow.mp3", "Waveform - 0.75x")

# Audio Fast
st.subheader("Fast Playback (1.5x)")
st.audio("file_example_MP3_1MG-fast.mp3")
plot_waveform("file_example_MP3_1MG-fast.mp3", "Waveform - 1.5x")
