import re
import time
import dataset
from intentToPattern import intentToPattern

class LyricsBot:
    def __init__(self):
        self.name = None

    def greetUser(self):
        """Gets the user's name and initiates conversation with them"""
        self.name = input("Hello, I am LyricsBot! What is your name? ")
        print("Nice to meet you, {}!".format(self.name))
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
        print("\nSearching...")
        results = dataset.findSongContain(phrase)
        self.displayResults(results=results, message="containing \"{}\"".format(phrase))
        self.getQuery(prompt="What else would you like to find? ")

    def getSongsFromArtist(self, artist):
        print("\nSearching...")
        results = dataset.findSongWithArtist(artist)
        self.displayResults(results=results, message="by {}:".format(artist))
        self.getQuery(prompt="What else would you like to find? ")

    def getRandomSong(self):
        print("\nSearching...")
        # TODO

    def displayResults(self, results, message):
        if len(results) != 0:
            print("Found {} songs {}".format(len(results), message))
            for song in results:
                print("* {} - {}".format(song[0], song[1]))
            print()
        else:
            print("Found no matches, sorry :(")

    def noIntentFound(self):
        self.getQuery(prompt="Sorry {}, but I'm not sure what you're asking for. Could you elaborate? ".format(self.name))


if __name__ == "__main__":
    bot = LyricsBot()
    bot.greetUser()