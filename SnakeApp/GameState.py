
#gamestate.py
from SnakeApp.constants import *;
from SnakeApp.Snake import Snake;
from SnakeApp.FoodPellet import FoodPellet;
import random

class GameState:
	"""A class to hold the state and objects involved with the snake game

	Properties:
		size: a tuple that holds the (x,y) dimensions of the grid
		snake: the game snake object
		pellets: list of FoodPellet objects
		dir: current user direction
		has_lost: boolean- has user lost the game
		has_won: boolean- has user won the game

	"""



	def __init__(self, size):

		self.size = size;

		self.snake = Snake(pos=[13,20], bounds=(25,25));
		self.pellets = []
		self.pellets.append(FoodPellet())

		self.has_won = False;
		self.has_lost = False;

		self.dir = UP;

		self._tickNum = 0;
		self.tick_rate = 5;

	def check_collide(self):

		i = 0;
		for pellet in self.pellets:
			if self.snake.on_position(pellet.pos):
				return i
			i += 1
		return -1


	
	def pellet_color_scroll(self):
		return ((random.randint(0,255),random.randint(0,255),random.randint(0,255)));
	

	def tick(self):
		"""Actions for one step of the game. Update the state of the object to reflect changes"""

		#increment the number of ticks we've made
		self._tickNum += 1;


		#speed up every 100 ticks
		if self._tickNum % 100 == 0:
			self.tick_rate += 3

		#every 200 ticks, add another food pellet
		if self._tickNum % 200 == 0:
			self.pellets.append(FoodPellet())



		if len(self.pellets) == 0:
			self.pellets.append(FoodPellet())

		if self.check_collide() != -1:
			print(self.check_collide())
			self.snake.grow(self.dir)
			self.pellets.pop(self.check_collide());
		else:
			self.snake.move(self.dir)

		#if you collide with yourself, you lose
		if self.snake.has_collided_self:
			self.has_lost = True;









