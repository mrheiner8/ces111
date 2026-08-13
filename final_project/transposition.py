#--- transposition.py   
"""
Program: W05 Final Project Music Transposition Tool
Author: Michael Heiner

Description:
    The program gets the name of a target instrument, a source instrument, source key signature, source list of note names. Then transposes the key signature and note names for the target instrument. This tool is useful for musicians that need to transpose music that is written for a different instrument. 
"""
import csv

# Key Signature information
KEYS_INFO = {
    "c major": "C Major: 0 accidentals",
    "a minor": "A Minor: 0 accidentals",
    "g major": "G Major: 1 sharp (F#)",
    "e minor": "E Minor: 1 sharp (F#)",
    "d major": "D Major: 2 sharps (F#, C#)",
    "b minor": "B Minor: 2 sharps (F#, C#)",
    "a major": "A Major: 3 sharps (F#, C#, G#)",
    "f# minor": "F# Minor: 3 sharps (F#, C#, G#)",
    "e major": "E Major: 4 sharps (F#, C#, G#, D#)",
    "c# minor": "C# Minor: 4 sharps (F#, C#, G#, D#)",
    "b major": "B Major: 5 sharps (F#, C#, G#, D#, A#)",
    "g# minor": "G# Minor: 5 sharps (F#, C#, G#, D#, A#)",
    "f# major": "F# Major: 6 sharps (F#, C#, G#, D#, A#, E#)",
    "d# minor": "D# Minor: 6 sharps (F#, C#, G#, D#, A#, E#)",
    "c# major": "C# Major: 7 sharps (F#, C#, G#, D#, A#, E#, B#)",
    "a# minor": "A# Minor: 7 sharps (F#, C#, G#, D#, A#, E#, B#)",
    "f major": "F Major: 1 flat (Bb)",
    "d minor": "D Minor: 1 flat (Bb)",
    "bb major": "Bb Major: 2 flats (Bb, Eb)",
    "g minor": "G Minor: 2 flats (Bb, Eb)",
    "eb major": "Eb Major: 3 flats (Bb, Eb, Ab)",
    "c minor": "C Minor: 3 flats (Bb, Eb, Ab)",
    "ab major": "Ab Major: 4 flats (Bb, Eb, Ab, Db)",
    "f minor": "F Minor: 4 flats (Bb, Eb, Ab, Db)",
    "db major": "Db Major: 5 flats (Bb, Eb, Ab, Db, Gb)",
    "bb minor": "Bb Minor: 5 flats (Bb, Eb, Ab, Db, Gb)",
    "gb major": "Gb Major: 6 flats (Bb, Eb, Ab, Db, Gb, Cb)",
    "eb minor": "Eb Minor: 6 flats (Bb, Eb, Ab, Db, Gb, Cb)",
    "cb major": "Cb Major: 7 flats (Bb, Eb, Ab, Db, Gb, Cb, Fb)",
    "ab minor": "Ab Minor: 7 flats (Bb, Eb, Ab, Db, Gb, Cb, Fb)",
}

# Chromatic Scale with sharps 
NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Chromatic Scale with flats
FLAT_NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

# Flat inputs -> Standard Sharp Scale
# Rare sharp inputs -> Natural Scale
NOTE_TRANSLATION = {
    "BB": "A#",
    "DB": "C#",
    "EB": "D#",
    "GB": "F#",
    "AB": "G#",
    "CB": "B",
    "FB": "E",   
    "E#": "F",
    "B#": "C"
}

def main():
    """Asks the user for input (starting instrument/key, target instrument/key, input file) and displays the results."""

    # Call the reading function and store the result
    instruments_dict = read_instruments("instruments.csv")

    # Get instrument input
    target_instrument_input = input("What is your target instrument of choice?: ") 
    source_instrument_input = input("What instrument is your source music written for?: ") 

    # get offset variables
    source_offset = get_instrument_name(source_instrument_input, instruments_dict)
    target_offset = get_instrument_name(target_instrument_input, instruments_dict)

    #calculate net offset
    net_offset =  source_offset - target_offset

    # get key input
    key_name = input('What key is your source music in? (Use a lower case"b" for flat. Use "#" for sharp and specify major or minor. EX "C# major"): ') 

    #get note input
    source_notes = input("What are the note names you need transposed (separated by commas, e.g., c, d#, eb): ") 

    # parse the source notes list
    clean_source_notes = []
    # Check if commas exist first 
    if "," in source_notes:
        for note in source_notes.split(","):
            # ignore empty spaces
            if note.strip():
                clean_source_notes.append(note.strip())

    # If no commas, check for spaces
    elif " " in source_notes:
        for note in source_notes.split():
            clean_source_notes.append(note.strip())
    # Single word/string with no spaces or commas
    else:
       clean_source_notes.append(source_notes.strip())

    key = key_name.split()
    root = key[0]
    mode = key[1]

    new_root = transpose_note(root, net_offset, use_flats=False)

    new_key = f"{new_root} {mode}".lower()

    target_key_description = get_key_signature_sharps_flats(new_key)

    if target_key_description is None:

        new_root = transpose_note(root, net_offset, use_flats=True)
        new_key = f"{new_root} {mode}".lower()

        target_key_description = get_key_signature_sharps_flats(new_key)

    print(f"\nYour transposed key signature is {target_key_description}")

    use_flats = "flat" in target_key_description.lower()

    try:
        notes_list = transpose_melody(clean_source_notes, net_offset, use_flats)
        output_notes_str = ", ".join(notes_list)
        print(f"\nYour transposed note names are: {output_notes_str}")
    except ValueError:
        print("Error: could not process notes")


def read_instruments(filename):
    """
    This function reads the instrument data from the csv file passed to the function in the filename parameter. The dictionary key is contained in the csv data column indicated by the key_column_index parameter, the value of each dictionary item is the list derived from the values in the row of the csv file. Function returns a dictionary of instruments.

    Parameters:
        filename: The path or name of the CSV file product information.

    Return Type:
        A dictionary where each key is an instrument name and each value is an integer representing the distance in transpositional relationship of the instrument to concert pitch in numbers of halftones.
    """
    instrument_dict = {}
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            instrument_name = row[0].strip().lower()
            key_offset = int(row[1])
            instrument_dict[instrument_name] = key_offset
    return instrument_dict  


def get_instrument_name(user_instrument_name, instrument_dict):
    """
    Takes the name of the provided instrument and assigns it a spot that is a distance away from concert pitch “C”. 
        
    Parameters:
        instrument_dict: The dictionary containing all instruments and their offset values.
        user_instrument_name: user provided instrument name use do look up a row in instrument_dict.
    Return Type:
        An int that will serve as the halftones reference in order to calculate the distance of transpositional relationship of the instrument to concert pitch.
    """ 
    clean_name = user_instrument_name.strip().lower()

    return instrument_dict.get(clean_name)


def get_key_signature_sharps_flats(key_name):
    """
    Takes a key name string (e.g., "G major") and returns the number of sharps or flats in the key signature (e.g., "+1 sharp") and lists their note names (e.g. F sharp). For the key of A major return A Major, 3 sharps; F sharp, C sharp, and G sharp 

    Parameters:
        key_name: user provided. name of the key that the source piece of music is written in. (major, or relative minor)
    Return Type:
        A str with key name and signature (the sharps or flats written on the staff) 
    """
    clean_key = key_name.strip().lower()
    
    return KEYS_INFO.get(clean_key)


def transpose_note(source_note, halftones, use_flats=False):
    """
    Takes a note string (e.g., "C") and integer shift (e.g., 2), and returns the new note (e.g., "D").

    Parameters:
        source_note: user provided. note name
        halftones: user provided. name of the key that the source piece of music is written in. (major, or relative minor)
        use_flats: bool (default False). Controls whether to return note names from FLAT_NOTES instead of NOTES.
    Return Type:
        A str with the new transposed note. 
    """
    #Clean up note name
    clean_note = source_note.strip().upper()

    # Swap it if it exists in NOTE_TRANSLATION:
    translated_note = NOTE_TRANSLATION.get(clean_note, clean_note)
    
    # find index position of source note
    index = NOTES.index(translated_note)

    # calculate new index and wraparound using modulo 12
    new_index =(index + halftones) % 12

    if use_flats:
        return FLAT_NOTES[new_index]
    else:
        return NOTES[new_index]


def transpose_melody(source_notes_list, halftones, use_flats=False):
    """Takes a list of notes and returns a new list with all notes transposed.
        
    Parameters:
        source_notes_list: user provided. list of note note names.
        halftones: user provided. name of the key that the source piece of music is written in. (major, or relative minor)
        use_flats: bool (default False). Controls whether to return note names from FLAT_NOTES instead of NOTES.
    Return Type:
        A list of strings representing the transposed notes.
    """
    # Create a list to store the transposed results
    new_transposed_melody = []

    # Loop over every note in source_notes_list. Call transpose_note(note, halftones) for each note append the returned string to transposed_melody.append the returned string to transposed_melody.
    for note in source_notes_list:
        new_note = transpose_note(note, halftones, use_flats)
        new_transposed_melody.append(new_note)

    # Return transposed_melody.
    return new_transposed_melody

# Call main to start this program.
if __name__ == "__main__":
    main()
#--- End transposition.py