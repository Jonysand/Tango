import mido
import numpy as np
import matplotlib.pyplot as plt

mid = mido.MidiFile('TANGO.mid')
maxInChord = 0
ticks = 1920   # set the ticks where the song starts
note_list = [] # storing all kinds of notes in this music
all_note = []  # storing all the notes in this music

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
#        print (msg.note)
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
#            print ("----")

note_list = np.asarray(note_list)
note_list.sort()
print ()
print (note_list)

"""-----------
Get the matrix

Initial state not included
"""
transMatrix = np.zeros((len(note_list), len(note_list)), dtype=float)
# go through all the notes, and adds up where two notes are adjacent
for i, each_note in enumerate(all_note):
    if i>(len(all_note)-2) :
        break
    index_of_this_note = np.where(note_list == each_note)[0][0]
    index_of_next_note = np.where(note_list == all_note[i+1])[0][0]
    transMatrix[index_of_this_note][index_of_next_note]+=1
# turn the matrix into probability
note_count = 0
cumsum = 0.0
for i in range(len(note_list)):
    note_count = np.sum(transMatrix, axis=1)[i]
    cumsum = 0
    for j in range(len(note_list)):
        cumsum += transMatrix[i][j]/note_count
        transMatrix[i][j] = cumsum
    note_count = 0

#testNote = 10
#plt.figure(figsize=(12,8))
#plt.plot(transMatrix[testNote])
#print ("probability of note ", note_list[testNote], " is ", transMatrix[testNote])
#plt.title("Cumulative Distribution function")
#plt.show()

np.savetxt('transMatrix.csv', transMatrix, delimiter=',')
