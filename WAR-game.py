import random

suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "JACK", "QUEEN", "KING", "ACE")
Value = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
         'JACK': 10, 'QUEEN': 10, 'KING': 10, 'ACE': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Value[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add(self, new_card):
        if type(new_card) == type([]):
            return self.hand.extend(new_card)
        else:
            return self.hand.append(new_card)

    def remove(self):
        return self.hand.pop(0)

    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards.'


# new_player = player('zanaty')
# new_deck = Deck()
# new_deck.shuffle()
# new_card = new_deck.deal_card()
# new_player.add([new_card,new_card,new_card,new_card])
# new_player.remove()
# print(new_player)
player1 = player('zanaty')
player2 = player('aly')
new_deck = Deck()
new_deck.shuffle()
# for x in range(26):
#     player1.add(new_deck.deal_card())
#     player2.add(new_deck.deal_card())
round_num = 0
game_on = True
while game_on:
    round_num += 1
    print(f'Round {round_num} Start!')
    if len(player1.hand) == 0:
        print('Player one is Lost! payer Two wins')
        game_on = False
        break
    elif len(player2.hand) == 0:
        print('Player two is Lost! payer One wins')
        game_on = False
        break
    player_one_card = []
    player_one_card.append(player1.remove())

    player_two_card = []
    player_two_card.append(player2.remove())
    at_war = True
    while at_war:
        if player_one_card[-1].value > player_two_card[-1].value:
            player1.add(player_one_card)
            player1.add(player_two_card)
            at_war = False

        elif player_one_card[-1].value < player_two_card[-1].value:
            player2.add(player_one_card)
            player2.add(player_two_card)
            at_war = False
        else:
            print('WAR!!')
        if len(player1.hand) < 5:
            at_war = False
            print('Player one Lost! payer Two wins')
        elif len(player2.hand) < 5:
            print('Player two Lost! payer')
            at_war = False
        else:
            for num in range(5):
                player_one_card.append(player1.remove())
                player_two_card.append(player2.remove())
