#--- transposition.py   


def main():
    # Asks the user for input (starting instrument/key, target instrument/key, input file) and displays the results.

import csv

def read_instruments(instruments):
    instrument_dict = {}
    with open(instruments, "rt") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            instrument_name = row[0].strip().lower()
            key_offset = int(row[1])
            instrument_dict[instrument_name] = key_offset
    return instrument_dict        


def get_instrument_name(inst_name):
    #Takes the name of the provided instrument and assigns it a spot that is a distance away from “C”


    """
    2. get_key_signature_sharps_flats(key_name)
        Takes a key name string (e.g., "G major") and returns the number of sharps or flats in the key signature (e.g., "+1 sharp") and lists their note names (e.g. F sharp). For the key of A major return A Major, 3 sharps; F sharp, C sharp, and G sharp 

    3. transpose_note(note, semitones)
        Takes a note string (e.g., "C") and integer shift (e.g., 2), and returns the new note (e.g., "D").

    4. transpose_melody(notes_list, semitones)
        Takes a list of notes and returns a new list with all notes transposed.

    5. read_notes_file(filename)
        Opens and reads a text file containing song notes into a list."""

# Call main to start this program.
if __name__ == "__main__":
    main()
#--- End transposition.py