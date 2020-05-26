
import pygame;
from SnakeApp.constants import *
from SnakeApp.GameState import GameState

# Size of the screen
SCREEN_TITLE = 'SnakeGame';

# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255);
RED_COLOR = (255,0,0);
BLUE_COLOR= (0,0,255);
BLACK_COLOR = (0, 0, 0);
BLUE_COLOR = (0,0,255);


# Clock used to update game events and frames
clock = pygame.time.Clock();
TICK_RATE = 5;
pygame.font.init();



class Game:
	"""Game manager class. Stores details about the overall game state and serves as the
		entry point for game execution"""

	TICK_RATE = 60



	def __init__(self, size=(800,800)):
		"""Game state initialization

		KeywordArguments:
		size-- size of the game window in pixels as a tuple:(x,y)
			default 800x800 px

		"""
		self.title = 'Snake';

		self.game_state = GameState((25,25));

		self.grid_rect_size = min(size[0],size[1])//25;
		self.margin = self.grid_rect_size * 0.1;
		self.grid_rect_size -= self.margin;

		self.screen = pygame.display.set_mode(size);
		pygame.display.set_caption(SCREEN_TITLE);


		self.done = False;





	def run(self):
		"""Run the game loop"""


		while not self.done:
			

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True;
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.game_state.dir = UP;
					if event.key == pygame.K_DOWN:
						self.game_state.dir = DOWN;
					if event.key == pygame.K_LEFT:
						self.game_state.dir = LEFT;
					if event.key == pygame.K_RIGHT:
						self.game_state.dir = RIGHT;


			
			self.game_state.tick();


			

			#draw the screen
			self.draw();
			pygame.display.flip();
			

			clock.tick(TICK_RATE);

			

		pygame.quit();



	def draw(self):

		self.screen.fill(BLACK_COLOR);


		for r in range(self.game_state.size[0]):
				for c in range(self.game_state.size[1]):
					col = WHITE_COLOR;
					if self.game_state.snake.on_position([r,c]):
						col = RED_COLOR;
					for pellet in self.pellets:
						if pellet.on_position([r,c]):
							col = BLUE_COLOR;

					pygame.draw.rect(self.screen, col,
						[(self.margin + self.grid_rect_size) * r + self.margin,
						 (self.margin + self.grid_rect_size) * c + self.margin,
						 self.grid_rect_size,
						 self.grid_rect_size])



