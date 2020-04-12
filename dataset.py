import pandas as pd
import re

csvFile = r"./songdata.csv"
songdata = pd.read_csv(csvFile)

# Lowercase
songdata["artist_lowercase"] = songdata["artist"].str.lower()

# Lowercase
songdata["song_lowercase"] = songdata["song"].str.lower()

# Lowercase and replace \n with ""
songdata["lyrics_clean"] = songdata["text"].str.lower()
songdata["lyrics_clean"] = songdata["lyrics_clean"].str.replace("\\n", "")

ARTIST_ORIG = "artist"
SONG_ORIG = "song"
LYRICS_ORIG = "text"
ARTIST = "artist_lowercase"
SONG = "song_lowercase"
LYRICS = "lyrics_clean"

def findSongContain(word):
    pat = phraseToRegex(word)
    songsDf = songdata[songdata[LYRICS].str.match(pat)]
    songsDf = songsDf.sample(frac=1) # return all rows in random order
    songs = songsDf[[SONG_ORIG, ARTIST_ORIG]].values.tolist()
    return songs

def findSongWithArtist(artist):
    pat = phraseToRegex(artist)
    songsDf = songdata[songdata[ARTIST].str.match(pat)]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG_ORIG, ARTIST_ORIG]].values.tolist()
    return songs

def findSongSongNameContain(word):
    pat = phraseToRegex(word)
    songsDf = songdata[songdata[SONG].str.match(pat)]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG_ORIG, ARTIST_ORIG]].values.tolist()
    return songs

def findSongContainBy(word, artist):
    lyricsPat = phraseToRegex(word)
    artistPat = phraseToRegex(artist)
    songsDf = songdata[songdata[LYRICS].str.match(lyricsPat) and songdata[ARTIST].str.match(artistPat)]
    songsDf = songsDf.sample(frac=1)
    songs = songsDf[[SONG_ORIG, ARTIST_ORIG]].values.tolist()
    return songs

def randomSongs(songCnt):
    songsDf = songdata.sample(n=songCnt)
    songs = songsDf[[SONG_ORIG, ARTIST_ORIG]].values.tolist()
    return songs

def phraseToRegex(phrase):
    phrase = phrase.strip() # Remove leading and trailing whitespace
    phrase = " ".join(phrase.split())   # Remove extra whitespace in between
    pat = ".*\\b" + phrase.replace(" ", ".*\\b") + ".*"
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



    
    