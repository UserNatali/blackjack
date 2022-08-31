import abc
import random


class AbstractPlayer(abc.ABC):
    def __init__(self, position):
        self.cards = []
        self.position = position
        self.bet = 0
        self.full_points = 0

    def chainge_points(self):
        self.full_points = sum([card.points for card in self.cards])

    def ack_card(self, deck, card_count):
        for _ in range(card_count):
            card = deck.get_card()
            self.cards.append(card)
        self.chainge_points()
        return True



    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    def print_cards(self):
        for card in self.cards:
            print(card)


class Player(AbstractPlayer):
    def change_bet(self, max_bet, min_bet):
        while True:
            valua = int(input('Make your bet: '))
            if valua > min_bet and valua < max_bet:
                self.bet = valua
                break
        print('Your bet is: ', self.bet)

# class Dealler(AbstractPlayer):
#     pass


class Bot(AbstractPlayer):
    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        print(self, 'give: ', self.bet)
