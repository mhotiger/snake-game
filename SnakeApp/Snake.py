#Snake.py
from SnakeApp.constants import *
from collections import deque;


class Snake:


	def __init__(self, pos, bounds):
		self.bounds = bounds;
		self.head = pos[:];
		self.list = deque([pos]);
		self.list.append([pos[0],pos[1]-1]);
		self.list.append([pos[0],pos[1]-2]);
		
		self.collided_self = False;


	def move(self, dir):
		"""moves the snake by one position in the direction given"""
		#TODO: change head based on the direction
		try:
			assert(dir == UP or dir == DOWN or dir == LEFT or dir == RIGHT)
		except:
			print("ERROR: Invalid Direction");
			return;
		
		if dir == UP:
			self.head[1] += 1;
		elif dir == DOWN:
			self.head[1] -= 1;
		elif dir == LEFT:
			self.head[0] += 1;
		elif dir == RIGHT:
			self.head[0] -= 1;


		head_mod = [self.head[0] % self.bounds[0], self.head[1] % self.bounds[0]];

		#add the new head to the front of the list, and remove the tail of the list- moves us one square over
		#modulo should wrap the head position of the snake when we reach the bounds of the frame
		self.list.appendleft(head_mod);
		self.list.pop();
		if self.list.count(head_mod) > 1:
			self.collided_self = True;
		
	def on_position(self, pos):
		"""Returns whether the snake is on a given tile"""
		return self.list.count(pos);


	def grow(self, dir):
		"""grows the snake in the given direction from the tail of the snake"""
		pass;

