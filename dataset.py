import pandas as pd

csvFile = r"./songdata.csv"
songdata = pd.read_csv(csvFile)

songdata["artist_lowercase"] = songdata["artist"].str.lower()
songdata["song_lowercase"] = songdata["song"].str.lower()
songdata["lyrics_lowercase"] = songdata["text"].str.lower()

ARTIST = "artist"
SONG = "song"
LYRICS = "text"
ARTIST_LOWER = "artist_lowercase"
SONG_LOWER = "song_lowercase"
LYRICS_LOWER = "lyrics_lowercase"

def findSongContain(word):
    songsDf = songdata[[word in lyric for lyric in songdata[LYRICS_LOWER]]]
    songsDf = songsDf.sample(frac=1) # return all rows in random order
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def findSongWithArtist(artist):
    songsDf = songdata[[artist in song for song in songdata[ARTIST_LOWER]]]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def findSongSongNameContain(word):
    songsDf = songdata[[word in song for song in songdata[ARTIST_LOWER]]]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def findSongContainBy(word, artist):
    songsDf = songdata[[word in lyric for lyric in songdata[LYRICS_LOWER]] and [artist in song for song in songdata[ARTIST_LOWER]]]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def randomSongs(songCnt):
    songsDf = songdata.sample(n=songCnt)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
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



    
    