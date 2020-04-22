import re
import string
import dataset
from intents import intentToPattern


RANDOM_SONG_COUNT = 10


class LyricsBot:
    def __init__(self):
        self.name = None

    def greetUser(self):
        """Gets the user's name and initiates conversation with them"""
        self.name = input("Hello, I am LyricsBot! What is your name? ")
        print("Nice to meet you, {}!".format(self.name), end=" ")
        self.getQuery()

    def getQuery(self, userMessage):
        """Gets query from the user or quits the app"""
        reply = userMessage.lower()
        if self.userWantsToQuit(reply):
            return self.quit()
        else:
            return self.getIntent(reply)

    def userWantsToQuit(self, reply):
        """Returns a boolean value that represents if the user wants to quit the app"""
        for pattern in intentToPattern["userWantsToQuit"]:
            foundMatch = re.match(pattern, reply)
            if foundMatch:
                return True
        return False

    def quit(self):
        """Quits the application"""
        return {"intent": "quit", "results": [], "entity": None}

    def getIntent(self, reply):
        """Gets the user's intent and calls relevant helper function"""
        for intent, patterns in intentToPattern.items():
            for pattern in patterns:
                foundMatch = re.match(pattern, reply)
                if foundMatch and intent == "findSongsContainingPhrase":
                    return self.getSongsContainingPhrase(phrase=foundMatch.group(1))
                elif foundMatch and intent == "findSongsFromArtist":
                    return self.getSongsFromArtist(artist=foundMatch.group(1))
                elif foundMatch and intent == "findRandomSong":
                    return self.getRandomSongs()
        return self.noIntentFound()

    def getSongsContainingPhrase(self, phrase):
        """Queries the dataset and displays songs with a particular word or phrase"""
        results = dataset.findSongContain(phrase)
        return {"intent": "getSongsContainingPhrase", "results": results, "entity": string.capwords(phrase)}

    def getSongsFromArtist(self, artist):
        """Queries the dataset and displays songs by a particular artist"""
        results = dataset.findSongWithArtist(artist)
        return {"intent": "getSongsFromArtist", "results": results, "entity": string.capwords(artist)}

    def getRandomSongs(self):
        """Queries the dataset and displays a few random songs"""
        results = dataset.randomSongs(RANDOM_SONG_COUNT)
        return {"intent": "getRandomSongs", "results": results, "entity": None}

    def noIntentFound(self):
        """Asks user to try asking the LyricBot again because an intent was not found"""
        return {"intent": "noIntentFound", "results": "", "entity": None}


if __name__ == "__main__":
    bot = LyricsBot()
    bot.greetUser()