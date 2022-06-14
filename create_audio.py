from scipy.io.wavfile import write
import numpy as np

  
samplerate = 44100

def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 #Frequency of Note C4
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0
    
    return note_freqs

def get_wave(freq, duration):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def get_song_data(music_notes, duration):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note], duration) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song.astype(np.int16)


def create_solo(music_notes, duration):
    try:   
        data = get_song_data(music_notes, duration)
        data = data * (16300/np.max(data))
        write('audio.wav', samplerate, data.astype(np.int16))
    except:
        print("Ocorreu um problema na geração do audio")


if __name__=='__main__':
    print("Estou na main")
    

    

