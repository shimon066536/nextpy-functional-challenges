import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }


notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

new_notes = notes.split("-")

yonatan_hakatan = (winsound.Beep([freqs[i] for i in [i[0] for i in [note.split(',') for note in new_notes]]][i], [int(i[1]) for i in [note.split(',') for note in new_notes]][i]) for i in range(len(new_notes)))

[i for i in yonatan_hakatan]
