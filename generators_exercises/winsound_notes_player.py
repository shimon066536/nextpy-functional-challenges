"""
winsound_notes_player.py

Plays a melody using the winsound module and a frequency mapping.
"""

import winsound

freqs = {
    "la": 220,
    "si": 247,
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
    "sol": 392,
}

def parse_notes(note_string):
    note_list = note_string.split("-")
    for note in note_list:
        tone, dur = note.split(",")
        yield freqs[tone], int(dur)

def play_song(song):
    for freq, dur in parse_notes(song):
        winsound.Beep(freq, dur)

def main():
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    play_song(notes)

if __name__ == "__main__":
    main()
