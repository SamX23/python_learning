from random import shuffle

class Card:
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # override less than operands
    # print(object < object)
    def __it__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    # override greater than operands
    # print(object < object)
    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    # Override magic method if you print object only
    # print(object)
    def __repr__(self):
        return self.values[self.value] + ' of ' + self.suits[self.suit]


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = 'Bot XP'
        name2 = 'Bot Ios'
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print('Lets have a Card Wars!\n')
        response = None
        while len(cards) >= 2 and response != 'q':
            response = input('\nPress enter next round, q to quit.\n')
            player1_card = self.deck.remove()
            player2_card = self.deck.remove()
            print('{} drew {} {} drew {}'
                  .format(self.player1.name, player1_card,
                          self.player2.name, player2_card))
            if player1_card > player2_card:
                self.player1.wins += 1
                print('{} win this round'.format(self.player1.name))
            else:
                self.player2.wins += 1
                print('{} win this round'.format(self.player2.name))
            print('War is over, {} wins'.format(self.winner(self.player1, self.player2)))

    @staticmethod
    def winner(player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "it was a tie"


play = Game()
play.play_game()
