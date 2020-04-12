import pandas as pd
import re

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
    pat = phraseToRegex(word)
    songsDf = songdata[songdata[LYRICS_LOWER].str.match(pat)]
    songsDf = songsDf.sample(frac=1) # return all rows in random order
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def findSongWithArtist(artist):
    pat = phraseToRegex(artist)
    songsDf = songdata[songdata[ARTIST_LOWER].str.match(pat)]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def findSongSongNameContain(word):
    pat = phraseToRegex(word)
    songsDf = songdata[songdata[SONG_LOWER].str.match(pat)]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def findSongContainBy(word, artist):
    lyricsPat = phraseToRegex(word)
    artistPat = phraseToRegex(artist)
    songsDf = songdata[songdata[LYRICS_LOWER].str.match(lyricsPat) and songdata[ARTIST_LOWER].str.match(artistPat)]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def randomSongs(songCnt):
    songsDf = songdata.sample(n=songCnt)
    songs = songsDf[[SONG, ARTIST]].values.tolist()
    return songs

def phraseToRegex(phrase):
    phrase = phrase.strip() # Remove leading and trailing whitespace
    phrase = " ".join(phrase.split())   # Remove extra whitespace in between
    pat = re.sub(" ", ".*", phrase)
    return pat


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



    
    