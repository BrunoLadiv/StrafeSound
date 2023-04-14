import sounddevice as sd
import soundfile as sf
import numpy as np
import keyboard

sound_path = "./Shoot.wav"

# Load the sound file
data, sample_rate = sf.read(sound_path)

# Set the playback speed
playback_speed = 2.0  # Double the playback speed
resampled_data = np.zeros(int(len(data) / playback_speed), dtype=data.dtype)
for i in range(len(resampled_data)):
    resampled_data[i] = data[int(i * playback_speed)]

# Define the key handlers
def play_sound(key):
    sd.play(resampled_data, sample_rate)

keyboard.on_release_key("a", lambda _: play_sound("a"))
keyboard.on_release_key("d", lambda _: play_sound("d"))

# Keep the script running
keyboard.wait()
