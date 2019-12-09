import csv

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        return 0

    def showdown(self, game_state):
        with open('log.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            for row in game_state:
                writer.writerow(row)

        # check our cards
        our_hand = []
        for row in game_state["players"]:
            if row["name"] == "NAND":
                our_hand.append(row["hole_cards"][0]["rank"])
                our_hand.append(row["hole_cards"][1]["rank"])

        if our_hand[0] == our_hand[1]:
            return 500


