from ast import Break
from tokenize import Double
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyaudio
import numpy as np
from PIL import Image
import random
import math
import playsound

img = mpimg.imread('constellations.jpg')
'''
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
#plt.imshow(imgGray)
plt.imshow(imgGray, cmap='gray')
plt.show()'''

image = Image.open('constellations.jpg', 'r')
pix_val = list(image.getdata())
result = []
#print(result)
for i in range(0, len(pix_val)):
    sum = 0
    for j in range(0, len(pix_val[i])):
        sum += pix_val[i][j]
    ave = sum / 3
    result.append(ave)

pix_val_flat = [x for sets in pix_val for x in sets]
#print(max(result))
x = max(result)
#print(len(result))
#print(len(pix_val)) 

freqs_1 = []

with open('frequency.txt') as txt:
    f = txt.readline()
    while f:
        f = txt.readline()
        try:
            freqs_1.append(float(f.strip()))
        except:
            print(" ")

#print(freqs_1)
while (len(freqs_1) != x):
    for i in range(0, len(freqs_1)):
        if (len(freqs_1) == x): break
        freqs_1.append(freqs_1[i])

#print(len(freqs_1))
#print(len(result))

# attempt 1
'''
p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 100000       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float


for i in range(len(result)):
    f = freqs_1[result[i]]
    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)d

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples)

    #stream.stop_stream()
    #stream.close()

p.terminate() '''

# option 1, attempt 2
def sine(frequency, length, rate):
    length = int(length * rate)
    factor = (float(frequency) * (math.pi * 2) / rate)
    return np.sin(np.arange(length) * factor)


def play_tone(stream, frequency, length, rate=44100):
    chunks = [sine(frequency, length, rate)]

    chunk = np.concatenate(chunks) * 0.25

    fade = 200.

    fade_in = np.arange(0., 1., 1/fade)
    fade_out = np.arange(1., 0., -1/fade)

    chunk[:fade] = np.multiply(chunk[:fade], fade_in)
    chunk[-fade:] = np.multiply(chunk[-fade:], fade_out)

    stream.write(chunk.astype(np.float32).tostring())


def test():
    for i in range(len(result)):
        freq = freqs_1[result[i]]
        play_tone(stream, freq, 0.1)


if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=2, rate=44100, output=2)

# option 2
def play_music():
    playsound.playsound("Galaxy_Music.mp3")


print("Menu: \n 1: intergalctic space adventure \n 2: soothing galaxy adventure\n")
n = int(input("Which adventure will you pick? "))

if n == 1:
    print("\nYou picked the intergalactic space adventure! Hold on tight...\n\n\n")
    test()
else:
    print("\nYou picked the soothing galaxy adventure! Sit back and relax...\n\n\n")
    for i in range(6):
        play_music()

