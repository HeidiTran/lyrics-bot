intentToPattern = {
    "userWantsToQuit": [
        r".*nothing.*",
        r".*quit.*",
        r".*done.*",
        r".*finish.*",
        r".*exit.*",
    ],
    "findSongsContainingPhrase": [
        r".*songs?.*go like\s(.*)",
        r".*lyrics[:\s]*(.*)",
        r".*songs?.*words?\s(.*)",
        r".*songs?.*contain(?:ing)?\s(.*)",
        r".*songs?.*with.*(?:phrase|words?)?\s(.*)",
        r".*songs?.*about\s(.*)",
    ],
    "findSongsFromArtist": [
        r".*songs?.*from\s(.*)",
        r".*songs?.*by\s(.*)",
    ],
    "findRandomSong": [
        r".*random.*songs?.*",
        r".*songs?.*anything.*",
        r".*recommend.*songs?.*",
        r".*suggest.*songs?.*",
    ]
}

yesPatterns = [
    r".*ye*s?.*",
    r".*ok.*",
    r".*sure.*",
    r".*yeah.*",
    r".*yup.*",
]