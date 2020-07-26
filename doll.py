import pygal
from random import randint


class Die():
    def __init__(self, choice_num=6):
        self.choice_num = choice_num

    def roll_on(self):
        return randint(1, self.choice_num)

