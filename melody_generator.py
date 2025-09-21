# ---------------------------
# Scale + MIDI logic
# ---------------------------
root_to_midi = {
    "C": 60,  "C#": 61, "D": 62,  "D#": 63, "E": 64, "F": 65,
    "F#": 66, "G": 67,  "G#": 68, "A": 69,  "A#": 70, "B": 71
}
midi_to_note = {v % 12: k for k, v in root_to_midi.items()}

scales_intervals = {
    "Major":             [0, 2, 4, 5, 7, 9, 11],
    "Natural Minor":     [0, 2, 3, 5, 7, 8, 10],
    "Harmonic Minor":    [0, 2, 3, 5, 7, 8, 11],
    "Melodic Minor":     [0, 2, 3, 5, 7, 9, 11],
    "Pentatonic Major":  [0, 2, 4, 7, 9],
    "Pentatonic Minor":  [0, 3, 5, 7, 10],
    "Blues":             [0, 3, 5, 6, 7, 10],
    "Dorian":            [0, 2, 3, 5, 7, 9, 10],
    "Phrygian":          [0, 1, 3, 5, 7, 8, 10],
    "Lydian":            [0, 2, 4, 6, 7, 9, 11],
    "Mixolydian":        [0, 2, 4, 5, 7, 9, 10],
    "Locrian":           [0, 1, 3, 5, 6, 8, 10],
    "Whole Tone":        [0, 2, 4, 6, 8, 10],
    "Chromatic":         list(range(12))
}

def get_scale(root: str, scale: str, octave: int = 4):
    base = root_to_midi[root] + (octave - 4) * 12
    intervals = scales_intervals[scale]
    midi_notes = [base + i for i in intervals]

    note_names = []
    for n in midi_notes:
        name = midi_to_note[n % 12]
        octv = (n // 12) - 1
        note_names.append(f"{name}{octv}")

    return midi_notes, note_names