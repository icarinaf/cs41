from ast import Break
from tokenize import Double
import pyaudio
import numpy as np
from PIL import Image
import random
import math
import playsound

scale_notes = {
    # pitch standard A440 ie a4 = 440Hz
    'c': 16.35,
    'C': 17.32,
    'd': 18.35,
    'D': 19.45,
    'e': 20.6,
    'f': 21.83,
    'F': 23.12,
    'g': 24.5,
    'G': 25.96,
    'a': 27.5,
    'A': 29.14,
    'b': 30.87
}

note_names = 'cCdDefFgGaAb'


def playnote(note, chord_style):
    if chord_style == "min":
        chord_tones = [0,3,7]
    elif chord_style == "maj":
        chord_tones = [0,4,7]
    elif chord_style == "five":
        chord_tones = [0,7]
    else:
        chord_tones = [0]

    num_notes = len(chord_tones)

    p = pyaudio.PyAudio()  # initialize pyaudio

    # sampling rate
    sample_rate = 22050

    LENGTH = 1  # seconds to play sound

    frames = int(sample_rate * LENGTH)

    wavedata = ''

    # generating waves
    stream = p.open(
        format=p.get_format_from_width(1),
        channels=1,
        rate=sample_rate,
        output=True)

    CHUNK = 256

    octave = int(note[1])
    frequencies = []
    for tone in chord_tones:
        chord_note = note_names.index(note[0]) + tone
        if chord_note<12:
            chord_note = note_names[chord_note]
            frequencies.append(scale_notes[chord_note] * (2**(octave + 1)))
            print(frequencies)
        else:
            chord_note = note_names[chord_note-12]
            frequencies.append( scale_notes[chord_note] * (2**(octave + 2)))
            print(frequencies)

    y = 0
    for x in range(frames//CHUNK):
        n=0
        wavedata=b''
        while n<CHUNK:
            wave=0
            for freqs in frequencies:
                wave += math.sin((y) / ((sample_rate / freqs) / math.pi)) * 127 + 128
            wave = wave/num_notes
            wavedata += bytes([int(wave)])
            y+=1
            n+=1

        stream.write(wavedata)

    stream.stop_stream()
    stream.close()
    p.terminate()


song = []
while True:
    song_composing = True
    note = ''
    while note != 'p':
        note = str(input(
            'Enter note (a-G) (capital for sharp) and an octave (0-8) or any other key to play: '))
        if note[0] in scale_notes:
            chord_style = str(
                input('Enter chord quality (maj, min, five): '))
            song.append((note, chord_style))
            playnote(note, chord_style)

    for chord in song:
        playnote(chord[0], chord[1])
    break
