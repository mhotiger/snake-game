
#gamestate.py
from SnakeApp.constants import *;
from SnakeApp.Snake import Snake;
from SnakeApp.FoodPellet import FoodPellet;


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

	def check_collide(self):
		for pellet in self.pellets:
			if self.snake.on_position(pellet.pos):
				return True
	def tick(self):
		"""Actions for one step of the game. Update the state of the object to reflect changes"""

		#increment the number of ticks we've made
		self._tickNum += 1;

		

		if len(self.pellets) == 0:
			self.pellets.append(FoodPellet())
		if self.check_collide():

			self.snake.grow(self.dir)
			self.pellets.pop();
		else:
			self.snake.move(self.dir)

			self.pellets.pop()








