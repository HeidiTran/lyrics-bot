intentToPattern = {
    "userWantsToQuit": [
        r".*nothing.*",
        r".*quit.*",
        r".*done.*",
        r".*finish.*",
        r".*exit.*",
        r"no.*",
    ],
    "findSongsContainingPhrase": [
        r".*songs?.*go like\s(.*)",
        r".*lyrics[:\s]*(.*)",
        r".*songs?.*words?\s(.*)",
        r".*songs?.*contain(?:ing)?\s(.*)",
        r".*songs?.*with.*(?:phrase|words?)\s(.*)",
        r".*songs?.*about\s(.*)",
    ],
    "findSongsFromArtist": [
        r".*songs?.*from\s(.*)",
        r".*songs?.*by\s(.*)",
    ],
    "findSongsContainingPhraseFromArtist": [
        r".*songs?.*go like\s(.*)\s(?:from|by)\s(.*)",
        r".*lyrics[\s]*(.*)\s(?:from|by)\s(.*)",
        r".*songs?.*words?\s(.*)\s(?:from|by)\s(.*)",
        r".*songs?.*contain(?:ing)?\s(.*)\s(?:from|by)\s(.*)",
        r".*songs?.*with.*(?:phrase|words?)\s(.*)\s(?:from|by)\s(.*)"
        r".*songs?.*about\s(.*)\s(.*)\s(?:from|by)\s(.*)",
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