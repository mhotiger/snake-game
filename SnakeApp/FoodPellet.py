#FoodPellet.py
from SnakeApp.constants import *

import random

class FoodPellet:

    def __init__(self):
        self.bounds = (25,25);
        self.x= random.randint(0,24)
        self.y= random.randint(0,24)
        self.pos = [self.x,self.y]
        self.apple_exists = True

    def on_position(self, pos):
        """Returns whether the snake is on a given tile"""
        if pos == self.pos:
            return True
    def do_nothing(self):
        pass

