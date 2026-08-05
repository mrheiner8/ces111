#--- test_transposition.py
from transposition import get_instrument_name
"""
from transposition import transpose_note
from transposition import get_key_signature_sharps_flats
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


"""
def test_transpose_note():
def test_get_key_signature_sharps_flats():
def test_transpose_melody():
"""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
#--- End test_transposition.py