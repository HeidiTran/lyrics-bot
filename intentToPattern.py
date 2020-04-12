intentToPattern = {
    "userWantsToQuit": [
        r".*nothing.*",
        r".*quit.*",
        r".*done.*",
        r".*finish.*",
    ],

    "findSongsContainingPhrase": [
        r".*songs?.*go like\s(.*)",
        r".*lyrics[:\s]*(.*)",
        r".*songs?.*words?\s(.*)",
        r".*songs?.*contain(?:ing)?\s(.*)",
        r".*songs?.*with\s(.*)",
    ],
    "findSongsFromArtist": [
        r".*songs?.*from\s(.*)",
        r".*songs?.*by\s(.*)",
    ],
    "findRandomSong": [
        r".*random.*songs?.*",
        r".*songs?.*anything.*",
        r".*recommend.*songs?.*",
    ]
}