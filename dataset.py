import pandas as pd

csvFile = r"./songdata.csv"
songdata = pd.read_csv(csvFile)

def findSongContain(word):
    songs = songdata[[word in lyric for lyric in songdata["text"]]]
    return songs

def findSongWithArtist(artist):
    songs = songdata[[artist in song for song in songdata["artist"]]]
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



    
    