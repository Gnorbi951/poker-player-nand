from copy import deepcopy


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

        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        sorted_list = deepcopy(community_cards) + deepcopy(our_hand)
        sorted_list = [values.index(i) for i in sorted_list]
        sorted_list.sort()
        counter = 1
        for index, card in enumerate(sorted_list):
            if card + 1 == sorted_list[index + 1]:
                counter += 1
            else:
                counter = 1
            if counter == 5:
                return 6000

        if False is not True:
            pass
        if our_hand[0] == our_hand[1] or our_hand[0] in community_cards or our_hand[
            1] in community_cards:  # pair in hand or in community cards
            return 750 if max(bets) < 750 else max(bets)
        if our_hand[0] in community_cards and our_hand[1] in community_cards:
            return 750 if max(bets) < 750 else max(bets)
        if game_state["round"] == 2 and (our_hand[0] != our_hand[1] or our_hand[0] not in community_cards or
                                         our_hand[1] not in community_cards):
            return 0

        return 11

    def showdown(self, game_state):
        pass
        # check our cards




