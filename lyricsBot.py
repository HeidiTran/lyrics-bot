import re
from intentToPattern import intentToPattern

class LyricsBot:
    def __init__(self):
        self.name = None

    def greetUser(self):
        """Gets the user's name and initiates conversation with them"""
        self.name = input("Hello, I am LyricsBot! What is your name?\n")
        print("Nice to meet you, {}!".format(self.name))
        self.getQuery()

    def getQuery(self, prompt="What would you like to find?\n"):
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
                if foundMatch and intent == "findSongsAboutTopic":
                    self.findSongsAboutTopic(topic=foundMatch.group(1))
                    return
                elif foundMatch and intent == "findSongsContainingPhrase":
                    self.findSongsContainingPhrase(phrase=foundMatch.group(1))
                    return
                elif foundMatch and intent == "findSongsFromArtist":
                    self.findSongsFromArtist(artist=foundMatch.group(1))
                    return
                elif foundMatch and intent == "findRandomSong":
                    self.findRandomSong()
                    return
        
        self.noIntentFound()

    def findSongsAboutTopic(self, topic):
        print("{} wants to find songs about {}".format(self.name, topic))
        self.getQuery(prompt="What else would you like to find?\n")

    def findSongsContainingPhrase(self, phrase):
        print("{} wants to find songs containing {}".format(self.name, phrase))
        self.getQuery(prompt="What else would you like to find?\n")

    def findSongsFromArtist(self, artist):
        print("{} wants to find songs from {}".format(self.name, artist))
        self.getQuery(prompt="What else would you like to find?\n")

    def findRandomSong(self):
        print("{} wants to find a random song to listen to!".format(self.name))

    def noIntentFound(self):
        self.getQuery(prompt="Sorry {}, but I'm not sure what you're asking for. Could you elaborate?".format(self.name))


if __name__ == "__main__":
    bot = LyricsBot()
    bot.greetUser()