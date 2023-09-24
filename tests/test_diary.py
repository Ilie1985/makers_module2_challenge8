# File: test_diary.py

import pytest
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

@pytest.fixture
def diary():
    return Diary()

def test_add_entry(diary):
    entry = DiaryEntry("Title", "Contents")
    diary.add(entry)
    assert len(diary.all()) == 1

def test_count_words(diary):
    entry1 = DiaryEntry("Title1", "This is a test entry")
    entry2 = DiaryEntry("Title2", "Another entry with more words")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == entry1.count_words() + entry2.count_words()

def test_reading_time(diary):
    entry1 = DiaryEntry("Title1", "This is a test entry")
    entry2 = DiaryEntry("Title2", "Another entry with more words")
    diary.add(entry1)
    diary.add(entry2)
    
    wpm = 200  # Adjust this value as needed
    expected_reading_time = entry1.reading_time(wpm) + entry2.reading_time(wpm)
    
    assert diary.reading_time(wpm) == expected_reading_time

def test_find_best_entry_for_reading_time(diary):
    entry1 = DiaryEntry("Title1", "This is a test entry")
    entry2 = DiaryEntry("Title2", "Another entry with more words")
    diary.add(entry1)
    diary.add(entry2)
    
    wpm = 200  # Adjust this value as needed
    minutes = 30  # Adjust this value as needed
    
    best_entry = diary.find_best_entry_for_reading_time(wpm, minutes)
    
    assert best_entry is not None
    assert best_entry.reading_time(wpm) <= minutes


