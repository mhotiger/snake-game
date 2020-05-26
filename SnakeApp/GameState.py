<<<<<<< Updated upstream
#gamestate.py
=======
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
		self.pellets = FoodPellet();

		self.has_won = False;
		self.has_lost = False;

		self.dir = UP;

		self._tickNum = 0;


	def tick(self):
		"""Actions for one step of the game. Update the state of the object to reflect changes"""

		#increment the number of ticks we've made
		self._tickNum += 1;

		self.snake.move(self.dir);

		if self.pellets.apple_exists == False:
			self.pellets=FoodPellet()







>>>>>>> Stashed changes
