from __future__ import division
import math
import sys
import os
import time


# p = pyaudio.PyAudio()
#os version
# 20 - 20,000 hertz
intensities = []
duration = 2000 # milliseconds

# os.system('clear')
name = input("Please enter your full name:")

print(f"Welcome to the frequency test, {name}")


print("This sound is what is considered as hearing an intensity of 5")
time.sleep(7)
os.system('play -n synth %s sin %s' % (duration/1000, 3500))



time.sleep(5)
frequency = [20, 50, 100, 200, 500, 800, 1000, 1500, 2000, 5000, 10000, 12000, 15000, 17000, 18000, 18500, 18800, 19000, 19500, 20000]


for i in frequency:
    # os.system('clear')
    input("Here is the baseline sound: (press ENTER to continue)")
    os.system('play -n synth %s sin %s' % (duration/1000, 3500))
    
    input("Here is a test sound: (press ENTER to continue)")
    
    os.system('play -n synth %s sin %s' % (duration/1000, i))
    
    score = input("rate test sound's intensity from 1-10 and Hit ENTER")
