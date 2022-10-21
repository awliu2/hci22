from __future__ import division
import math
import sys
import os


from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import matplotlib.pylab as plt

import time

import numpy as np
import pyaudio

# p = pyaudio.PyAudio()

# volume = 0.5  # range [0.0, 1.0]
# fs = 44100  # sampling rate, Hz, must be integer
# duration = 5.0  # in seconds, may be float
# f = 18000.0  # sine frequency, Hz, may be float

# # generate samples, note conversion to float32 array
# x = 2 * np.pi * np.arange(fs * duration) * f / fs
# samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)


# plt.plot(x, samples)
# plt.xlabel('Angle [rad]')
# plt.ylabel('sin(x)')
# plt.axis('tight')
# plt.show()
# # per @yahweh comment explicitly convert to bytes sequence
# output_bytes = (volume * samples).tobytes()

# # for paFloat32 sample values must be in range [-1.0, 1.0]
# stream = p.open(format=pyaudio.paFloat32,
#                 channels=1,
#                 rate=fs,
#                 output=True)

# # play. May repeat with different volume values (if done interactively)
# start_time = time.time()
# stream.write(output_bytes)
# print("Played sound for {:.2f} seconds".format(time.time() - start_time))

# stream.stop_stream()
# stream.close()

# p.terminate()


#Generate 1k,2k,3k tones of 3 sec duration
#tone1 = Sine(1000).to_audio_segment(duration=3000)
#tone2 = Sine(2000).to_audio_segment(duration=3000)
#tone3 = Sine(3000).to_audio_segment(duration=3000)

#Append each tone onto other with crossfade
#multitone = tone1.append(tone2, crossfade=2500).append(tone3, crossfade=2500)


#Play final tone
#play(multitone)

#song = AudioSegment.from_wav("alarm.wav")
#play(song)

#os version
# 20 - 20,000 hertz
print("Frequency test")
duration = 2000 # milliseconds
print("This sound is what is considered as hearing an intensity of 10")
time.sleep(7)
os.system('play -n synth %s sin %s' % (duration/1000, 3500))

time.sleep(5)
frequency = [20, 50, 100, 200, 500, 800, 1000, 1500, 2000, 5000, 10000, 12000, 15000, 17000, 18000, 18500, 18800, 19000, 19500, 20000]

for i in frequency:
    os.system('play -n synth %s sin %s' % (duration/1000, i))
    time.sleep(5)
    print("Enter in intensity")

#20, 50, 100,    