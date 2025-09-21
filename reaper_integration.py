import os
import random

# Create a new track
RPR_InsertTrackAtIndex(0, True)
track = RPR_GetTrack(0, 0)

# Create a new MIDI item directly on the track
item_start = 0.0
item_length = 4.0  # 4 beats
item = RPR_CreateNewMIDIItemInProj(track, item_start, item_start + item_length, False)
take = RPR_GetMediaItemTake(item, 0)

# Melody generation parameters
root_note = 60  # Middle C
scale = [0, 2, 4, 5, 7, 9, 11]  # Major scale intervals
num_notes = 8
melody = [root_note + random.choice(scale) for _ in range(num_notes)]

# Note timing - work in quarter notes and convert
beats_per_note = 0.5  # eighth notes
ppq = 960  # Standard PPQ, but we'll convert io

# Insert notes
for i, note in enumerate(melody):
    # Calculate timing in quarter notes, then convert to PPQ
    start_qn = i * beats_per_note
    end_qn = start_qn + beats_per_note
    
    start_ppq = RPR_MIDI_GetPPQPosFromProjQN(take, start_qn)
    end_ppq = RPR_MIDI_GetPPQPosFromProjQN(take, end_qn)
    
    inserted = RPR_MIDI_InsertNote(
        take,
        False,      # selected
        False,      # muted
        int(start_ppq),  # start position in PPQ
        int(end_ppq),    # end position in PPQ
        0,          # channel (0-15)
        note,       # pitch (0-127)
        100,        # velocity (1-127)
        False       # no sort yet
    )
    
    if not inserted:
        RPR_ShowMessageBox(f"Failed to insert note {note} at QN {start_qn}", "Insert Error", 0)

# Finalize
RPR_MIDI_Sort(take)
RPR_UpdateItemInProject(item)
RPR_UpdateArrange()

# Show results
RPR_ShowMessageBox(f"Inserted melody: {melody}\nNotes: {len(melody)}", "Success", 0)