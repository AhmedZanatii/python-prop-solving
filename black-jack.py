import random

suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "JACK", "QUEEN", "KING", "ACE")
Value = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
         'JACK': 10, 'QUEEN': 10, 'KING': 10, 'ACE': 11}


class card:
    def __init__(self, suit, rank, ):
        self.suit = suit
        self.rank = rank
        self.value = Value[self.rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add(self, new_card):
        return self.hand.append(new_card)

    def __str__(self):
        return f'{self.name} has {self.hand}'


player1 = player(input('Enter your name:\n '))
player2 = player('DEALER')
sum1 = 0
sum2 = 0
new_deck = deck()
new_deck.shuffle()
player1.add(new_deck.deal_card())
player1.add(new_deck.deal_card())
player2.add(new_deck.deal_card())
player2.add(new_deck.deal_card())

game_on = True
while game_on:
    for card in range(len(player1.hand)):
        print(player1.hand[card], end=' , ')
    z = input('\nWould you like to continue? (y/n) ')
    if z.lower() == 'y':
        player1.add(new_deck.deal_card())
        player2.add(new_deck.deal_card())
    elif z.lower() == 'n':

        game_on = False
        for card in range(len(player1.hand)):
            sum1 += player1.hand[card].value
            sum2 += player2.hand[card].value
        if sum1 == sum2:
            print('no one win!')
            print(sum2)
        elif sum1 > 21 >= sum2:
            print('The dealer wins!')
            print(sum2)
        elif sum1 > 21 and sum2 > 21:
            if sum1 > sum2:
                print('The dealer wins!')
                print(sum2)
            elif sum2 > sum1:
                print('you win')
                print(sum2)
        elif sum1 < 21 < sum2:
            print('you win')
            print(sum2)
        elif sum2 < 21 and sum1 < 21:
            if sum1 > sum2:
                print('you win')
                print(sum2)
            elif sum2 > sum1:
                print('The dealer wins!')
                print(sum2)
