
import pygame;

# Size of the screen
SCREEN_TITLE = 'SnakeGame';

# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255);
RED_COLOR = (255,0,0);
BLUE_COLOR= (0,0,255);
BLACK_COLOR = (0, 0, 0);


# Clock used to update game events and frames
clock = pygame.time.Clock();
TICK_RATE = 60;
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


		self.grid_rect_size = min(size[0],size[1])//25;
		self.margin = self.grid_rect_size * 0.1;
		self.grid_rect_size -= self.margin;

		self.screen = pygame.display.set_mode(size);
		pygame.display.set_caption(SCREEN_TITLE);


		self.done = False;





	def run(self):
		"""Run the game loop"""


		while not self.done:
			self.screen.fill(WHITE_COLOR);

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True;

<<<<<<< Updated upstream
			for r in range(25):
				for c in range(25):
					pygame.draw.rect(self.screen,WHITE_COLOR,
						[(self.margin + self.grid_rect_size) * c + self.margin,
						 (self.margin + self.grid_rect_size) * r + self.margin,
						 self.grid_rect_size,
						 self.grid_rect_size])
=======
			self.draw();
			self.game_state.tick();
>>>>>>> Stashed changes

			clock.tick(TICK_RATE);

			pygame.display.flip();

		pygame.quit();


<<<<<<< Updated upstream
=======
	def draw(self):

		for r in range(25):
				for c in range(25):
					col = WHITE_COLOR;

					if self.game_state.snake.on_position([r,c]):
						col = RED_COLOR;
					if self.game_state.pellets.on_position([r,c]):
						col = BLUE_COLOR;
					pygame.draw.rect(self.screen, col,
						[(self.margin + self.grid_rect_size) * c + self.margin,
						 (self.margin + self.grid_rect_size) * r + self.margin,
						 self.grid_rect_size,
						 self.grid_rect_size])

>>>>>>> Stashed changes

