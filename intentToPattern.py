intentToPattern = {
    "userWantsToQuit": [
        r".*nothing.*",
        r".*quit.*",
        r".*done.*"
    ],
    "findSongsAboutTopic": [
        r".*songs?.*about\s(.*)",
        r".*songs?.*related?\sto\s(.*)"
    ],
    "findSongsContainingPhrase": [
        r".*songs?.*go like\s(.*)",
        r".*lyrics[:\s]*(.*)",
        r".*songs?.*words?\s(.*)",
    ],
    "findSongsFromArtist": [
        r".*songs?.*from\s(.*)",
        r".*songs?.*by\s(.*)",
    ],
    "findRandomSong": [
        r".*random.*songs?.*",
        r".*songs?.*anything.*",
        r".*recommend.*songs?.*"
    ]
}