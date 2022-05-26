import numpy as np
import simpleaudio as sa
import matplotlib.image as mpimg
from PIL import Image
NOTES = {
    "C0":16.35,
    "E0":20.60,
    "G0":24.50,
    "C1":32.70,
    "E1":41.20,
    "G1":49.00,
    "C2":65.41,
    "E2":82.41,
    "G2":98.00,
    "C3":130.81,
    "E3":164.81,
    "G3":196.00,
    "C4":261.63,
    "E4":329.63,
    "G4":392.00,
    "C5":523.25,
    "E5":659.25,
    "G5":783.99,
    "C6":1046.50,
    "E6":1318.51,
    "G6":1567.98,
    "C7":2093.00,
    "E7":2637.02,
    "G7":3135.96,
    "C8":4186.01,
    "E8":5274.04,
    "G8":6271.93
}

# calculate note frequencies
def find_pixel_ave(pixel):
    average = 0
    for i in range(0, len(pixel)):
        average += pixel[i]
    return average / 3

grayscale_image = 'IMG_0821.jpeg'
color_image = 'IMG_3189.jpg'
small_image = 'IMG_0276.jpeg'
andy_warhol = 'images/8-andy-warhol-new-york-artist.jpg'
colors = 'images/image.png'
squidward = 'images/squidward.jpg'
starry_night = 'images/starry_night.jpeg'

image = Image.open(color_image, 'r')
row_length, num_rows = image.size
pix_val = list(image.getdata())
#pix_val = [[0,0,0],[1,1,1],[2,2,2]]
result = []
rows = []
#print(result)
temp = 0
for i in range(0, len(pix_val)):
    if (i % row_length == 0):
        val = int(temp / row_length)
        rows.append(val)
        temp = 0
    else:
        temp += np.average(pix_val[i])

temp = 0
for i in range(0, len(rows)):
    if (i % 9 == 0):
        val = int(temp / 9)
        result.append(val)
        temp = 0
    else:
        temp += rows[i]




all_rows = result

previous_val = -1
curr_octave = 5
row_index = 0
up_or_down = 1
while row_index < len(rows) - 1:
    curr_val = rows[row_index]
    if curr_val > previous_val:
        if up_or_down == -1:
            C_freq = NOTES["C" + str(curr_octave)]
            E_freq = NOTES["E" + str()]
            
        if up_or_down == 1:





















A_freq = 261.63
Csh_freq = 329.63
E_freq = 392.00
C5_freq = 523.25

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.75
t = np.linspace(0, T, int(T * sample_rate), False)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)
C5_note = np.sin(C5_freq * t * 2 * np.pi)

# mix audio together
audio = np.zeros((44100, 2))
n = len(t)
offset = 0
audio[0 + offset: n + offset, 0] += A_note
audio[0 + offset: n + offset, 1] += 0.125 * A_note
#offset = 0 to overlap notes completely
offset = 5500
audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
offset = 11000
audio[0 + offset: n + offset, 0] += 0.125 * E_note
audio[0 + offset: n + offset, 1] += E_note


# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

#  wait for playback to finish before exiting
play_obj.wait_done()

audio = np.zeros((44100, 2))
n = len(t)
offset = 0
audio[0 + offset: n + offset, 0] += E_note
audio[0 + offset: n + offset, 1] += 0.125 * E_note
#offset = 0 to overlap notes completely
offset = 5500
audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
offset = 11000
audio[0 + offset: n + offset, 0] += 0.125 * A_note
audio[0 + offset: n + offset, 1] += A_note


# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

# # wait for playback to finish before exiting
play_obj.wait_done()andy-warhol-new-york-artist.jpg'

colors = 'images/image.png'

squidward = 'images/squidward.jpg'

starry_night = 'images/starry_night.jpeg'

image = Image.open(color_image, 'r')
row_length, num_rows = image.size
pix_val = list(image.getdata())
#pix_val = [[0,0,0],[1,1,1],[2,2,2]]
result = []
rows = []
#print(result)
temp = 0
for i in range(0, len(pix_val)):
    if (i % row_length == 0):
        val = int(temp / row_length)
        rows.append(val)
        temp = 0
    else:
        temp += np.average(pix_val[i])

temp = 0
for i in range(0, len(rows)):
    if (i % 9 == 0):
        val = int(temp / 9)
        result.append(val)
        temp = 0
    else:
        temp += rows[i]




all_rows = result

previous_val = -1
curr_octave = 5
row_index = 0
up_or_down = 1
while row_index < len(rows) - 1:
    curr_val = rows[row_index]
    if curr_val > previous_val:
        if up_or_down == -1:
            C_freq = NOTES["C" + str(curr_octave)]
            E_freq = NOTES["E" + str()]
            
        if up_or_down == 1:





















A_freq = 261.63
Csh_freq = 329.63
E_freq = 392.00
C5_freq = 523.25

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.75
t = np.linspace(0, T, int(T * sample_rate), False)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)
C5_note = np.sin(C5_freq * t * 2 * np.pi)

# mix audio together
audio = np.zeros((44100, 2))
n = len(t)
offset = 0
audio[0 + offset: n + offset, 0] += A_note
audio[0 + offset: n + offset, 1] += 0.125 * A_note
#offset = 0 to overlap notes completely
offset = 5500
audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
offset = 11000
audio[0 + offset: n + offset, 0] += 0.125 * E_note
audio[0 + offset: n + offset, 1] += E_note


# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

#  wait for playback to finish before exiting
play_obj.wait_done()

audio = np.zeros((44100, 2))
n = len(t)
offset = 0
audio[0 + offset: n + offset, 0] += E_note
audio[0 + offset: n + offset, 1] += 0.125 * E_note
#offset = 0 to overlap notes completely
offset = 5500
audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
offset = 11000
audio[0 + offset: n + offset, 0] += 0.125 * A_note
audio[0 + offset: n + offset, 1] += A_note


# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

# # wait for playback to finish before exiting
play_obj.wait_done()
j.gepj.thgin_rrats/segami'' =th thgin_yrrayrratsgpj.drawdiuqs/segami'' = drawdiuqsItsetgnpacneld oy-warrhol-n=ewm-/yosrk-arti
est.'
iogag
 imag''ea = Image.ompeins(color_image, 'r')
row_length, num_rows = image.size
pix_val = list(image.getdata())
#pix_val = [[0,0,0],[1,1,1],[2,2,2]]
result = []
rows = []
#print(result)
temp = 0
for i in range(0, len(pix_val)):
    if (i % row_length == 0):
        val = int(temp / row_length)
        rows.append(val)
        temp = 0
    else:
        temp += np.average(pix_val[i])

temp = 0
for i in range(0, len(rows)):
    if (i % 9 == 0):
        val = int(temp / 9)
        result.append(val)
        temp = 0
    else:
        temp += rows[i]




all_rows = result

previous_val = -1
curr_octave = 5
row_index = 0
up_or_down = 1
while row_index < len(rows) - 1:
    curr_val = rows[row_index]
    if curr_val > previous_val:
        if up_or_down == -1:
            C_freq = NOTES["C" + str(curr_octave)]
            E_freq = NOTES["E" + str(curr_octave)]
            G_freq = NOTES["G" + str(curr_octave)]
        if up_or_down == 1:





















A_freq = 261.63
Csh_freq = 329.63
E_freq = 392.00
C5_freq = 523.25

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100
T = 0.75
t = np.linspace(0, T, int(T * sample_rate), False)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)
C5_note = np.sin(C5_freq * t * 2 * np.pi)

# mix audio together
audio = np.zeros((44100, 2))
n = len(t)
offset = 0
audio[0 + offset: n + offset, 0] += A_note
audio[0 + offset: n + offset, 1] += 0.125 * A_note
#offset = 0 to overlap notes completely
offset = 5500
audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
offset = 11000
audio[0 + offset: n + offset, 0] += 0.125 * E_note
audio[0 + offset: n + offset, 1] += E_note


# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

#  wait for playback to finish before exiting
play_obj.wait_done()

audio = np.zeros((44100, 2))
n = len(t)
offset = 0
audio[0 + offset: n + offset, 0] += E_note
audio[0 + offset: n + offset, 1] += 0.125 * E_note
#offset = 0 to overlap notes completely
offset = 5500
audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
offset = 11000
audio[0 + offset: n + offset, 0] += 0.125 * A_note
audio[0 + offset: n + offset, 1] += A_note


# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

# # wait for playback to finish before exiting
play_obj.wait_done()