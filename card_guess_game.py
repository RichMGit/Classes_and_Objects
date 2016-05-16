import random

class Card:
    def __init__(self):

        self.rank = {'1' : '1', '2' : '2', '3' : '3', '4' : '4', '5' : '5', '6' : '6',
                     '7' : '7', '8' : '8', '9' : '9', '10' : '10',
                     '11' : 'J', '12' : 'Q', '13' : 'K', '14' : 'A'}
        self.suit = ['C', 'D', 'H', 'S']
        self.suitab_to_suitfull = {'C' : 'Clubs', 'D' : 'Diamonds', 'H' : 'Hearts', 'S' : 'Spades'}

    # def get_random_card():
    #     return Card
class Player:
    def __init__(self):
        self.card = Card()

    def take_a_guess(self):
        random_card_rank = random.choice(list(self.card.rank.keys()))
        random_card_suit = random.choice(self.card.suit)
        # print(random_card_rank)
        # print(random_card_suit)
        guesses = 3
        while guesses != 0:
            try:
                rank_guess, suit_guess = input('Guess the card: ').split()
                if guesses == 3:
                    if rank_guess == random_card_rank and suit_guess.rstrip() == random_card_suit:
                        print('Wow, well done you got it in one')
                        break
                    else:
                        print('Nah')
                        suit_full = self.card.suitab_to_suitfull[random_card_suit]
                        print('The suit is ' + suit_full)
                        guesses -= 1
                elif guesses == 2:
                    guesses -= 1
                    if rank_guess > random_card_rank:
                        print('Rank is lower')
                    elif rank_guess < random_card_rank:
                        print('Rank is higher')
                    elif rank_guess == random_card_rank and suit_guess.rstrip() == random_card_suit:
                        print('Well done you got it!!!')
                        break
                    else:
                        print('i am none of these')
                elif guesses == 1:
                    guesses -= 1
                    print('You are ' + str(abs(int(rank_guess) - int(random_card_rank))) + ' away')
                elif guesses == 0:
                    print('You are out of guesses, the card was', str(random_card_rank + ' ' + random_card_suit))
            except ValueError:
                print('You cant do that! Try again...')


class Game:

    def __init__(self):
        self.player = Player()
    def start(self):
        self.player.take_a_guess()

game = Game()
game.start()
