from random import random
from scipy.io.wavfile import write
import numpy as np
from pydub import AudioSegment 
from pydub.playback import play 
  
samplerate = 44100

def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 #Frequency of Note C4
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0
    
    return note_freqs
def get_wave(freq, duration = random() + 0.1):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave
def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song.astype(np.int16)
def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()
    
    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)
    
    chord_data = np.concatenate(chord_data, axis=0)    
    return chord_data.astype(np.int16)
def create_solo(music_notes):
    try:
        data = get_song_data(music_notes)
        data = data * (16300/np.max(data))
        write('audio.wav', samplerate, data.astype(np.int16))
    except:
        print("Ocorreu um problema na geração do audio")
def play_audio(name):
    wav_file_1 = AudioSegment.from_file(name)  
    play(wav_file_1)
    
if __name__=='__main__':
    # main()
    create_solo("D-C-B-E-G-G-C-C-E-C-E-D-A-G-D-F-E-C-A-G")

    

