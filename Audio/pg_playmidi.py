""" based on 'PG_MidiBase64_py23.py' code (see link below)
experiments with module pygame from: http://www.pygame.org/
play a midi music file (base64 encoded)

(base64 encoding simply produces a readable string from binary data)
"""
import pygame
import base64
import io, os, sys, inspect
from pathlib import Path

### https://www.daniweb.com/programming/software-development/code/216979/embed-and-play-midi-music-in-your-code-python


def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    pygame.mixer.music.load(music_file)
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    # check if playback has finished
    while pygame.mixer.music.get_busy():
        clock.tick(30)


###############################################################################

argc = len(sys.argv)
if argc < 2:
    print('\nUsage: python pg_playmidi.py filename.mid\n')
    sys.exit(0)
    #filename = "galaxian.mid"
else:
    filename = sys.argv[1]  # argv[0] is the python script name

cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe())))
parent_folder = Path(cmd_folder).parent
midi_folder = os.path.join(parent_folder, "data", "midi");
print(f"MIDI FOLDER : {midi_folder}\nMIDI FILE   : {filename}")

music_file = os.path.join(midi_folder, filename)

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)

try:
    # use the midi file object from memory
    play_music(music_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit
