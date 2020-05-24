
import pygame;

# Size of the screen
SCREEN_TITLE = 'SnakeGame'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('helvetiva', 75)


Class Game:
	"""Game manager class. Stores details about the overall game state and serves as the
		entry point for game execution"""

	TICK_RATE = 60

	def __init__(self):
		"""Game state initialization"""
		pass


	def run(self):
		"""Run the game loop""";
		pass