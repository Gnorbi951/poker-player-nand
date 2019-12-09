import sys

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        return 250

    def showdown(self, game_state):
        sys.stdout(game_state)
        pass

