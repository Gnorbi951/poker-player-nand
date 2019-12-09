import sys

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        our_hand = []
        for row in game_state["players"]:
            if row["name"] == "NAND":
                our_hand.append(row["hole_cards"][0]["rank"])
                our_hand.append(row["hole_cards"][1]["rank"])

        if our_hand[0] == our_hand[1]:
            return 500
        return 250

    def showdown(self, game_state):
        sys.stdout(game_state)
        # check our cards


