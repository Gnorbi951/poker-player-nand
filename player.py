import csv

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        return 20

    def showdown(self, game_state):
        with open('log.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            for row in game_state:
                writer.writerow(row)
        pass

