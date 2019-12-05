import mido
import numpy as np

mid = mido.MidiFile('TANGO.mid')
maxInChord = 0
ticks = 1920
note_list = []
all_note = []

"""--------------
Get all the note
"""
for msg in mid.tracks[1]:
    '''
    get the highest note as the main melody
    '''
    if msg.type == "note_on":
        if msg.note>maxInChord:
            maxInChord = msg.note
    elif msg.type == "note_off" and msg.note == maxInChord:
        maxInChord = 0
        print (msg.note)
        all_note.append(msg.note)
        if msg.note not in note_list:
            note_list.append(msg.note)

    '''
    get the start of every sentence
    '''
    if msg.type == "note_on" or msg.type == "note_off":
        ticks += msg.time
        if (ticks >= 3840):
            ticks = 0
            print ("----")

note_list = np.asarray(note_list)
note_list.sort()
print ()
print (note_list)


"""-----------
Get the matrix
"""

