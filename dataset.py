import pandas as pd

csvFile = r"./songdata.csv"
songdata = pd.read_csv(csvFile)

songdata["artist_lowercase"] = songdata["artist"].str.lower()
songdata["song_lowercase"] = songdata["song"].str.lower()
songdata["lyrics_lowercase"] = songdata["text"].str.lower()

ARTIST_COL = "artist_lowercase"
SONG_COL = "song_lowercase"
LYRICS_COL = "lyrics_lowercase"

def findSongContain(word):
    songsDf = songdata[[word in lyric for lyric in songdata[LYRICS_COL]]]
    songs = songsDf[[SONG_COL, ARTIST_COL]].values.tolist()
    return songs

def findSongWithArtist(artist):
    songsDf = songdata[[artist in song for song in songdata[ARTIST_COL]]]
    songs = songsDf[[SONG_COL, ARTIST_COL]].values.tolist()
    return songs

def findSongSongNameContain(word):
    songsDf = songdata[[word in song for song in songdata[ARTIST_COL]]]
    songs = songsDf[[SONG_COL, ARTIST_COL]].values.tolist()
    return songs

def findSongContainBy(word, artist):
    songsDf = songdata[[word in lyric for lyric in songdata[LYRICS_COL]] and [artist in song for song in songdata[ARTIST_COL]]]
    songs = songsDf[[SONG_COL, ARTIST_COL]].values.tolist()
    return songs

if __name__ == "__main__":
    csvFile = r"./songdata.csv"
    songdata = pd.read_csv(csvFile)

    print("Shape (rows, columns):")
    print(songdata.shape)

    print("Info:")
    print(songdata.info())

    print("Columns:")
    print(songdata.columns)

    print("Index:")
    print(songdata.index)

    print("Summary statistics:")
    print(songdata.describe())

    print("Head:")
    print(songdata.head(10))

    print("Tail:")
    print(songdata.tail(10))

    print("Songs contain Heidi:")
    print(findSongContain("Heidi"))



    
    