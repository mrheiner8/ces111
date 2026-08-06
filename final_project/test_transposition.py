#--- test_transposition.py
from transposition import get_instrument_name
from transposition import get_key_signature_sharps_flats

from transposition import transpose_note
"""
from transposition import transpose_melody
"""
import pytest

def test_get_instrument_name():
    # Dummy test dictionary 
    sample_dict = {'trumpet': -2,'alto saxophone': 9,}

    # Test exact match
    assert get_instrument_name("alto saxophone", sample_dict) == 9

    # Test case/space handling
    assert get_instrument_name("  TRUMPET ", sample_dict) == -2

    # Test missing key
    assert get_instrument_name("melophone", sample_dict) is None


def test_get_key_signature_sharps_flats():
    # Test exact match
    assert get_key_signature_sharps_flats("c major") == "C Major: 0 accidentals"

    # Test case/space handling
    assert get_key_signature_sharps_flats("  G MAJOR ") == "G Major: 1 sharp (F#)"

    # Test missing key
    assert get_key_signature_sharps_flats("C Dorian") is None


def test_transpose_note():
    # Test exact match
    assert transpose_note("C", 3) == "D#"

    # Test case/space handling
    assert transpose_note("  c ",-2) == "A#"

    # Test 0
    assert transpose_note("C",0) == "C"

"""
def test_transpose_melody():
"""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
#--- End test_transposition.py