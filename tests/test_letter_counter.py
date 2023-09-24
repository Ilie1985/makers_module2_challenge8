from lib.letter_counter import *

# Test case for the calculate_most_common method
def test_calculate_most_common():
    # Test when the input text has a most common letter
    counter = LetterCounter("Digital Punk")
    result = counter.calculate_most_common()
    assert result == [2, "i"]



