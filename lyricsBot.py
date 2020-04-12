import re
import dataset
from intents import intentToPattern, yesPatterns

RANDOM_SONG_COUNT = 3
MAX_RESULT_LENGTH = 10

class LyricsBot:
    def __init__(self):
        self.name = None

    def greetUser(self):
        """Gets the user's name and initiates conversation with them"""
        self.name = input("Hello, I am LyricsBot! What is your name? ")
        print("Nice to meet you, {}!".format(self.name), end=" ")
        self.getQuery()

    def getQuery(self, prompt="What would you like to find? "):
        """Gets query from the user or quits the app"""
        reply = input(prompt).lower()
        if self.userWantsToQuit(reply):
            self.quit()
        else:
            self.getIntent(reply)

    def userWantsToQuit(self, reply):
        """Returns a boolean value that represents if the user wants to quit the app"""
        for pattern in intentToPattern["userWantsToQuit"]:
            foundMatch = re.match(pattern, reply)
            if foundMatch:
                return True
        return False

    def quit(self):
        """Quits the application"""
        print("Okay, see you next time, {}!".format(self.name))
        exit()

    def getIntent(self, reply):
        """Gets the user's intent and calls relevant helper function"""
        for intent, patterns in intentToPattern.items():
            for pattern in patterns:
                foundMatch = re.match(pattern, reply)
                if foundMatch and intent == "findSongsContainingPhrase":
                    self.getSongsContainingPhrase(phrase=foundMatch.group(1))
                    return
                elif foundMatch and intent == "findSongsFromArtist":
                    self.getSongsFromArtist(artist=foundMatch.group(1))
                    return
                elif foundMatch and intent == "findRandomSong":
                    self.getRandomSong()
                    return
        self.noIntentFound()

    def getSongsContainingPhrase(self, phrase):
        """Queries the dataset and displays songs with a particular word or phrase"""
        results = dataset.findSongContain(phrase)
        self.displayResults(results=results, message="containing \"{}\":".format(phrase.title()))
        self.getQuery(prompt="What else would you like to find? ")

    def getSongsFromArtist(self, artist):
        """Queries the dataset and displays songs by a particular artist"""
        results = dataset.findSongWithArtist(artist)
        self.displayResults(results=results, message="by {}:".format(artist.title()))
        self.getQuery(prompt="What else would you like to find? ")

    def getRandomSong(self):
        """Queries the dataset and displays a few random songs"""
        results = dataset.randomSongs(RANDOM_SONG_COUNT)
        self.displayResults(results=results, message="for you:")
        self.getQuery(prompt="What else would you like to find? ")

    def displayResults(self, results, message):
        """Prints the results of a query if there are any songs to display"""
        if len(results) != 0:
            plural = "songs" if len(results) > 1 else "song"
            print("\nFound {} {} {}".format(len(results), plural, message))
            if len(results) > MAX_RESULT_LENGTH:
                self.displayIncrementalResults(results=results)
            else:
                for song in results:
                    print("* {} - {}".format(song[0], song[1]))
            print()
        else:
            print("Found no matches, sorry :(\n")

    def displayIncrementalResults(self, results):
        """Breaks large search results into smaller, more readable chunks"""
        displayed = 10
        for i in range(MAX_RESULT_LENGTH):
            print("* {} - {}".format(results[i][0], results[i][1]))
        while displayed < len(results):
            reply = input("\nWould you like to see more results? ")
            for pattern in yesPatterns:
                foundMatch = re.match(pattern, reply)
                if foundMatch and displayed + 10 < len(results):
                    print("\nDisplaying 10 more results:")
                    for i in range(displayed, displayed + 10):
                        print("* {} - {}".format(results[i][0], results[i][1]))
                    displayed += 10
                    break
                elif foundMatch and displayed + 10 > len(results):
                    songsLeft = len(results) - displayed
                    plural = "results" if songsLeft > 1 else "result"
                    print("\nDisplaying {} more {}:".format(songsLeft, plural))
                    for i in range(displayed, len(results)):
                        print("* {} - {}".format(results[i][0], results[i][1]))
                    return
                else: 
                    return

    def noIntentFound(self):
        """Asks user to try asking the LyricBot again because an intent was not found"""
        self.getQuery(prompt="Sorry {}, I'm not sure what you're asking for. Could you say that again? ".format(self.name))


if __name__ == "__main__":
    bot = LyricsBot()
    bot.greetUser()