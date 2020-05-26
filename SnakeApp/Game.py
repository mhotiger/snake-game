
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
GREEN_COLOR = (0,255,0);


# Clock used to update game events and frames
clock = pygame.time.Clock();
TICK_RATE = 5;
pygame.font.init();

#starting the mixer
pygame.init()
bgmusic = pygame.mixer.Sound('snakeloop.wav')
crunch = pygame.mixer.Sound('crunch.wav')
gameover = pygame.mixer.Sound('gameover.wav')

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

		self.size = size;
		self.title = 'Snake';

		self.game_state = GameState((25,25));

		self.grid_rect_size = min(size[0],size[1])//25;
		self.margin = self.grid_rect_size * 0.1;
		self.grid_rect_size -= self.margin;

		self.screen = pygame.display.set_mode(size);
		pygame.display.set_caption(SCREEN_TITLE);
		self.font = pygame.font.Font('freesansbold.ttf', 32)


		self.done = False;
		pygame.mixer.Sound.play(bgmusic, -1)




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

			if self.game_state.check_collide() != -1:
				pygame.mixer.Sound.play(crunch)
			if self.game_state.has_won:
				self.won()
			if self.game_state.has_lost:
				
				self.lost()

			self.game_state.tick();


			#draw the screen
			self.draw();
			pygame.display.flip();


			clock.tick(self.game_state.tick_rate);



		pygame.quit();


	def won(self):
		
		while not self.done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True;


			self.screen.fill(GREEN_COLOR);
			text = self.font.render('You Won', True, BLACK_COLOR)
			text_rect = text.get_rect()
			text_rect.center = (self.size[0]//2, self.size[1]//2);
			self.screen.blit(text, text_rect)
			pygame.display.update();
			clock.tick(30);



		pygame.quit()


	def lost(self):

		pygame.mixer.Sound.stop(bgmusic)
		pygame.mixer.Sound.play(gameover)
		
		while not self.done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True;

			
			self.screen.fill(RED_COLOR);
			text = self.font.render('You Lost', True, BLACK_COLOR)
			text_rect = text.get_rect()
			text_rect.center = (self.size[0]//2, self.size[1]//2);
			self.screen.blit(text, text_rect)
			pygame.display.update();
			clock.tick(30);


			

		pygame.quit()







	def draw(self):

		self.screen.fill(BLACK_COLOR);


		for r in range(self.game_state.size[0]):
				for c in range(self.game_state.size[1]):
					col = WHITE_COLOR;
					if self.game_state.snake.on_position([r,c]):
						col = RED_COLOR;
					for pellet in self.game_state.pellets:
						if pellet.on_position([r,c]):
							col = self.game_state.pellet_color_scroll();

					pygame.draw.rect(self.screen, col,
						[(self.margin + self.grid_rect_size) * r + self.margin,
						 (self.margin + self.grid_rect_size) * c + self.margin,
						 self.grid_rect_size,
						 self.grid_rect_size])





