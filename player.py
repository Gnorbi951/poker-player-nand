import logging

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        logging.warning(game_state)
        our_hand = []
        community_cards = []
        try:
            for card in game_state["community_cards"]:
                community_cards.append(card[0]["rank"])
                community_cards.append(card[1]["rank"])
                community_cards.append(card[2]["rank"])
                community_cards.append(card[3]["rank"])
                community_cards.append(card[4]["rank"])
        except:
            pass

        for row in game_state["players"]:
            if row["name"] == "NAND":
                our_hand.append(row["hole_cards"][0]["rank"])
                our_hand.append(row["hole_cards"][1]["rank"])
        bets = []
        for player in game_state["players"]:
            if player["name"] != "NAND":
                bets.append(player["bet"])


        if our_hand[0] == our_hand[1] or our_hand[0] in community_cards or our_hand[1] in community_cards: # pair in hand or in community cards
            return 750 if max(bets) < 750 else max(bets)
        if our_hand[0] in community_cards and our_hand[1] in community_cards:
            return 750 if max(bets) < 750 else max(bets)

        if game_state["round"] == 1 and (our_hand[0] != our_hand[1] or our_hand[0] not in community_cards or
                                         our_hand[1] not in community_cards):
            return 0

        return 15

    def showdown(self, game_state):
        pass
        # check our cards


