from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        if isinstance(entry, DiaryEntry):
            self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry
        # Sum the word counts of all entries
        return sum(entry.count_words() for entry in self.entries)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        # Sum the reading times of all entries
        return sum(entry.reading_time(wpm) for entry in self.entries)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        best_entry = None
        min_difference = float('inf')

        for entry in self.entries:
            entry_reading_time = entry.reading_time(wpm)
            difference = abs(entry_reading_time - minutes)

            if entry_reading_time <= minutes and difference < min_difference:
                best_entry = entry
                min_difference = difference

        return best_entry