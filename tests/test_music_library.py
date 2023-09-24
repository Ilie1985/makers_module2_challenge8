import pytest
from lib.music_library import MusicLibrary
from lib.track import Track


# Fixture to create a library with sample tracks
@pytest.fixture
def sample_library():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    return library

def test_add_tracks(sample_library):
    assert len(sample_library.tracks) == 2

def test_search_by_title_existing_keyword(sample_library):
    results = sample_library.search_by_title("Way")
    assert len(results) == 1
    assert results[0].title == "Always The Hard Way"

def test_search_by_title_partial_keyword(sample_library):
    results = sample_library.search_by_title("lace")
    assert len(results) == 1
    assert results[0].title == "Higher Place"

def test_search_by_title_nonexistent_keyword(sample_library):
    results = sample_library.search_by_title("zzz")
    assert len(results) == 0

def test_format_track():
    track = Track("Higher Place", "Malevolence")
    formatted_track = track.format()
    assert formatted_track == "Higher Place by Malevolence"
