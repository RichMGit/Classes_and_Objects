from collections import OrderedDict

class Player:
    def __init__(self):
        self.biography = {'Name' : '', 'Age' : 0, 'Nationality' : '', 'Position' : '', 'Footed' : ''}
        self.attributes = {'Shooting' : 0, 'Passing' : 0, 'Tackling:' : 0, 'Acceleration:' : 0,
                           'Jumping' : 0, 'Crossing' : 0, 'Aggression' : 0, 'Volleying' : 0,
                           'Heading' : 0, 'Balance' : 0}
        self.bio_list = []

    def create_player(self):
        for key, value in self.biography._asdict.items():
            print(key, value, sep = ': ')


    def edit_bio(self):
        print('code for edit bio')

    def edit_attributes(self):
        points = 500
        print('You have ', str(points), 'points remaining')
        print('Each attribute has a maximum score of 100')
        while points > 0:
            chosen_attribute = input('Chose an attribute to add points to: ')
            if chosen_attribute in self.attributes:
                print('You have chosen', chosen_attribute)
                points_given = int(input('How many points do you wish to add to this: '))
                points_used = sum(self.attributes.values()) + points_given
                print(sum(self.attributes.values()))
                print(str(points - points_used), 'left')
                self.attributes[chosen_attribute] = self.attributes[chosen_attribute][values] + points_given
                if points - points_given > 0 and points_given <= 100:
                    print(self.attributes)
                else:
                    print('You cant add that many points')
            else:
                print(chosen_attribute, 'is not a valid attribute')



    def view_bio(self):
        print('view bio')

    def view_attributes(self):
        print('view attributes')

    def menu(self):
        while True:
            print('''
            0 - Quit
            1 - Create a player
            2 - Edit a players bio
            3 - Edit a players attributes
            4 - View a players bio
            5 - View a players attributes
            ''')
            option = int(input('What do you want to do? '))
            if option == 0:
                print('Come back soon!')
                break
            elif option == 1:
                self.create_player()
            elif option == 2:
                self.edit_bio()
            elif option == 3:
                self.edit_attributes()
            else:
                print('not a valid option')



class Game:
    def __init__(self):
        self.player = Player()

    def start(self):
        self.player.menu()

game = Game()
game.start()
