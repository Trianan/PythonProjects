# Notes-in-a-Chord Machine Version 0.1 by: Tristin Manson
# This section defines a list containing all notes in the 12-tone music system.
notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
print(notes)

# This section allows a user to input a root note, and chord type, and sets both as variables.
while True:
    root = input("Choose a note: ").title()
    print(f"Input: {root}")

    # This ensures user input for "root" is a valid character combination:
    acceptable_root_inputs = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A#",
                              "Bb", "C#", "Db", "D#", "Eb", "F#", "Gb", "G#", "Ab"]
    if root not in acceptable_root_inputs:
        print("Invalid input.")

    else:
        # This is supposed to derive, for example: "A#/Bb", from a user input of either "A#" or "Bb" separately.
        sharps_flats_compactor = ["A#", "Bb", "C#", "Db", "D#", "Eb", "F#", "Gb", "G#", "Ab"]
        if root in sharps_flats_compactor:
            print("Note is a sharp/flat...")
            compactor_index = int(sharps_flats_compactor.index(root))
            print(compactor_index)
# PAST THIS POINT, SOMETHING FISHY BE GOING ON!
# notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
            if compactor_index == (0 or 1):   # <--- This now doesn't set "A#" to "A#/Bb"
                root = notes[1]
            elif compactor_index == (2 or 3): # Neither does this???
                root = notes[4]
            elif compactor_index == (4 or 5):
                root = notes[6]
            elif compactor_index == (6 or 7):
                root = notes[9]
            elif compactor_index == (8 or 9):
                root = notes[11]

            # This section is proving way more difficult than I figured it would; input_value_index_gate.py is a -
            # - prototype version of this section that works correctly, so perhaps a solution can be found there.

        print(root)
        break

while True:
    chord_type = input("What type of chord?: ")
    # This section will apply the rules of musical-intervals to the index of "root", and through applying math -
    # - selects the correct indexes for the notes the type of chord based off the root note.
