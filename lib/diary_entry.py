class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string 

    def __init__(self, title, contents):# title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        # Split the contents into words by whitespace and return the count
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        # Calculate reading time based on word count and words per minute (wpm)
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        # Calculate the maximum number of words that can be read in 'minutes'
        # Calculate the maximum number of words that can be read in 'minutes'
        pass

        

        
        





        
        