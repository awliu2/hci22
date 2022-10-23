from __future__ import division

import os
import time
from random import shuffle

# p = pyaudio.PyAudio()
#os version
# 20 - 20,000 hertz
intensities = []
frequency = [20, 50, 100, 200, 500, 800, 1000, 1500, 2000, 5000, 10000, 12000, 15000, 17000, 18000, 18500, 18800, 19000, 19500, 20000]
scores = {}
for f in frequency:
    scores[f] = "-1"
shuffle(frequency)
duration = 1000 # milliseconds
os.system('clear')

name = input("Please enter your full name:\n")
os.system('clear')
print(f"Welcome to the frequency test, {name}")

time.sleep(2)
os.system('clear')

print(f"Here is the baseline sound.\n")
time.sleep(0.5)
os.system('play -n -q synth %s sin %s' % (duration/1000, 3500))
time.sleep(2)
print("The baseline sound is scored a 5 out of 10.\n")
time.sleep(2)
print("You will be rating frequencies on a scale of 1 - 10 based on its intensity.\n")
time.sleep(2)
print("A score of zero may be given if a frequency is inaudible.\n")
time.sleep(2)
print("If needed, you can press 'b' during the study to replay the benchmark sound.\n")
time.sleep(2)
input("---press ENTER to continue---")
os.system('clear')

for i, f in enumerate(frequency[:1]):
    rated = False
    heard_test = False
    while not rated:
        os.system('clear')
        print(f"---frequency {i + 1} of {len(frequency)}---")
        inp = input("'t' to play test sound\n'b' to hear the benchmark\n'c' to continue to rating \n")
        if inp == 'c':
            if not heard_test:
                print("You need to first play the test sound before rating.")
                time.sleep(1)
                continue
            scores[f] = input("rate test sound's intensity from 0 - 10: ")
            rated = True
            time.sleep(0.5)

        if inp == 'b':
            os.system('play -n -q synth %s sin %s' % (duration/1000, 3500))
            time.sleep(0.5)

        if inp == 't':
            heard_test = True
            os.system('play -n -q synth %s sin %s' % (duration/1000, f))
            time.sleep(0.5)

os.system('clear')
print("Thank you for participating in our study")
time.sleep(1)
input("---press ENTER to exit the program---")
os.system('clear')

file_name = name + '.csv'
with open(file_name, 'w') as out:
    out.write(name + "\n")

    for f, s in scores.items():
        out.write(str(f) + ',' + s)
        out.write("\n")