# https://younglinux.info/oopython/objects.php

import random

class Warrior(object):
    health = 100

    def __init__(self, name):
        self.name = name

    def do_attack(self):
        print(f'{self.name} attacked!')

    def get_harm(self):
        self.health -= 20
        print(f'{self.name} got harm! ')

    def get_health(self):
        if self.health == 0:
            print(f'{self.name} is dead...')
        else:
            print(f'{self.name} has got {self.health} point of health!')

    def get_winner(self):
        print(f'{self.name} won!!!!')


def let_the_war_begin(first, second):
    warrior_1 = Warrior(first)
    warrior_2 = Warrior(second)
    warriors = [warrior_1, warrior_2]

    while True:
        if warrior_1.health == 0:
            warrior_2.get_winner()
            break
        elif  warrior_2.health == 0:
            warrior_1.get_winner()
            break

        index = random.randint(0, 1)

        first_war = warriors[index]
        second_war = warriors[index - 1]

        first_war.do_attack()
        second_war.get_harm()
        second_war.get_health()


let_the_war_begin('Tom', 'Jerry')
