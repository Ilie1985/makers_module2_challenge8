# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks
    def __init__(self):
        
        self.tracks=[]

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        self.tracks.append(track)
    
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        list_of_tracks_with_keyword=[]
        for track in self.tracks:
            if keyword.lower() in track.title.lower():
                list_of_tracks_with_keyword.append(track)

        return list_of_tracks_with_keyword