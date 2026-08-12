#--- test_transposition.py
from transposition import get_instrument_name
from transposition import get_key_signature_sharps_flats

from transposition import transpose_note

from transposition import transpose_melody

import pytest

def test_get_instrument_name():
    # Dummy test dictionary 
    sample_dict = {'trumpet': -2,'alto saxophone': 9,}

    # Test exact match
    assert get_instrument_name("alto saxophone", sample_dict) == 9

    # Test case/space handling
    assert get_instrument_name("  TRUMPET ", sample_dict) == -2

    # Test missing key
    assert get_instrument_name("mellophone", sample_dict) is None


def test_get_key_signature_sharps_flats():
    # Test exact match
    assert get_key_signature_sharps_flats("c major") == "C Major: 0 accidentals"

    # Test case/space handling
    assert get_key_signature_sharps_flats("  G MAJOR ") == "G Major: 1 sharp (F#)"

    # Test for b (flats)
    assert get_key_signature_sharps_flats("bb major") == "Bb Major: 2 flats (Bb, Eb)"

    # test for # (sharps)
    assert get_key_signature_sharps_flats("f# minor") == "F# Minor: 3 sharps (F#, C#, G#)"

    # Test missing key
    assert get_key_signature_sharps_flats("C Dorian") is None


def test_transpose_note():
    # Test exact match
    assert transpose_note("C", 3) == "D#"

    # Test case/space handling
    assert transpose_note("  c ",-2) == "A#"

    # Test translation handling
    assert transpose_note("b#",-2) == "A#"

    # Test 0
    assert transpose_note("C",0) == "C"


def test_transpose_melody():
    sample = ["A#", "C", "D", "D#", "F", "G", "A"]    
    # Test positive integer (trumpet to alto saxophone)
    assert transpose_melody(sample, 5) == ["D#", "F", "G", "G#", "A#", "C", "D"]

    # Test negative integer (trumpet to flute)
    assert transpose_melody(sample, -2) == ["G#", "A#", "C", "C#", "D#", "F", "G"]

    # Test 0 (trumpet to clarinet)
    assert transpose_melody(sample, 0) == ["A#", "C", "D", "D#", "F", "G", "A"]


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
#--- End test_transposition.py