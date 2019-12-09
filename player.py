import logging

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        our_hand = []
        community_cards = []
        try:
            for card in game_state["community_cards"]:
                community_cards.append(card[0]["rank"])
                community_cards.append(card[1]["rank"])
                community_cards.append(card[2]["rank"])
        except:
            pass

        for row in game_state["players"]:
            if row["name"] == "NAND":
                our_hand.append(row["hole_cards"][0]["rank"])
                our_hand.append(row["hole_cards"][1]["rank"])

        if our_hand[0] == our_hand[1] or our_hand[0] in community_cards or our_hand[1] in community_cards :
            return 750
        return 250

    def showdown(self, game_state):
        logging.warning(game_state)
        # check our cards


