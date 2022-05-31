import numpy as np
import simpleaudio as sa
import matplotlib.image as mpimg
from PIL import Image
NOTES = {
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

def findRows(image_name):
    image = Image.open(image_name, 'r')
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
        if (i % 3 == 0):
            val = int(temp / 3)
            result.append(val)
            temp = 0
        else:
            temp += rows[i]
    return result



def play_notes_up(NOTES, curr_octave):
    C_freq = NOTES["C" + str(curr_octave)]
    E_freq = NOTES["E" + str(curr_octave)]
    G_freq = NOTES["G" + str(curr_octave)]

            # get timesteps for each sample, T is note duration in seconds
    sample_rate = 44100
    T = 0.75
    t = np.linspace(0, T, int(T * sample_rate), False)

            # generate sine wave notes
    C_note = np.sin(C_freq * t * 2 * np.pi)
    E_note = np.sin(E_freq * t * 2 * np.pi)
    G_note = np.sin(G_freq * t * 2 * np.pi)

            # mix audio together
    audio = np.zeros((44100, 2))
    n = len(t)
    offset = 0
    audio[0 + offset: n + offset, 0] += C_note
    audio[0 + offset: n + offset, 1] += 0.125 * C_note
            #offset = 0 to overlap notes completely
    offset = 5500
    audio[0 + offset: n + offset, 0] += 0.5 * E_note
    audio[0 + offset: n + offset, 1] += 0.5 * E_note
    offset = 11000
    audio[0 + offset: n + offset, 0] += 0.125 * G_note
    audio[0 + offset: n + offset, 1] += G_note

            # normalize to 16-bit range
    audio *= 32767 / np.max(np.abs(audio))
            # convert to 16-bit data
    audio = audio.astype(np.int16)

            # start playback
    play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

            #  wait for playback to finish before exiting
    play_obj.wait_done()


def play_notes_down(NOTES, curr_octave):
    C_freq = NOTES["C" + str(curr_octave)]
    E_freq = NOTES["E" + str(curr_octave)]
    G_freq = NOTES["G" + str(curr_octave)]

            # get timesteps for each sample, T is note duration in seconds
    sample_rate = 44100
    T = 0.75
    t = np.linspace(0, T, int(T * sample_rate), False)

            # generate sine wave notes
    C_note = np.sin(C_freq * t * 2 * np.pi)
    E_note = np.sin(E_freq * t * 2 * np.pi)
    G_note = np.sin(G_freq * t * 2 * np.pi)

            # mix audio together
    audio = np.zeros((44100, 2))
    n = len(t)
    offset = 0
    audio[0 + offset: n + offset, 0] += G_note
    audio[0 + offset: n + offset, 1] += 0.125 * G_note
            #offset = 0 to overlap notes completely
    offset = 5500
    audio[0 + offset: n + offset, 0] += 0.5 * E_note
    audio[0 + offset: n + offset, 1] += 0.5 * E_note
    offset = 11000
    audio[0 + offset: n + offset, 0] += 0.125 * C_note
    audio[0 + offset: n + offset, 1] += C_note

            # normalize to 16-bit range
    audio *= 32767 / np.max(np.abs(audio))
            # convert to 16-bit data
    audio = audio.astype(np.int16)

            # start playback
    play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

            #  wait for playback to finish before exiting
    play_obj.wait_done()


def playImage(image):
    rows = findRows(image)
    previous_val = -1
    curr_octave = 5
    row_index = 0
    up_or_down = 1

    while row_index < len(rows) - 1:
        curr_val = rows[row_index]

        # If the current row value is greater than the previous
        # row value, go up!
        if curr_val > previous_val:

            # If last "move" was a down, ascend but in current octave
            if up_or_down == -1:
                play_notes_up(NOTES, curr_octave)
                up_or_down = 1
            
            # If last "move" was an up, ascend in next highest octave
            elif up_or_down == 1:
                if curr_octave == 8:
                    play_notes_up(NOTES, curr_octave)
                else:
                    curr_octave += 1
                    play_notes_up(NOTES, curr_octave)
    
        # If the current row value is greater than the previous 
        # row value, go down
        elif curr_val < previous_val:

            # If last "move" was a down, descend an octave
            if up_or_down == -1:
                if curr_octave == 2:
                    play_notes_down(NOTES, curr_octave)
                else:
                    curr_octave -= 1
                    play_notes_down(NOTES, curr_octave)
        
            # If last move was an up, descend, but in the same octave
            elif up_or_down == 1:
                play_notes_down(NOTES, curr_octave)
                up_or_down = -1
        
        previous_val = curr_val
        row_index += 1

if __name__ == "__main__":
    val = input("Enter the filename for the image you want to play: ")
    playImage(val)