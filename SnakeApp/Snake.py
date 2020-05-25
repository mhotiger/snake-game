#Snake.py
from SnakeApp.constants import *
from collections import deque;


class Snake:


	def __init__(self, pos, bounds):
		"""Create a snake starting at position <pos>(positions are a list of [x,y] coordinates) with maximum bounds <bounds>(a list of [x,y] size of the board)"""
		self.bounds = bounds;
		self.head = pos[:]
		self.head_mod = pos[:]
		#list will store the list of coordinates the snake occupies. start off with 3 elements
		#add the head
		self.list = deque([pos]);
		#add an element one position down from the head
		self.list.append([ pos[0] , pos[1]-1 ] );
		#add an element 2 positions down from the head
		self.list.append([ pos[0] , pos[1]-2 ] );
		
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
			self.head[1] -= 1;
		elif dir == DOWN:
			self.head[1] += 1;
		elif dir == LEFT:
			self.head[0] -= 1;
		elif dir == RIGHT:
			self.head[0] += 1;


		self.head_mod = [self.head[0] % self.bounds[0], self.head[1] % self.bounds[0]];

		#add the new head to the front of the list, and remove the tail of the list- moves us one square over
		#modulo should wrap the head position of the snake when we reach the bounds of the frame
		self.list.appendleft(self.head_mod);
		self.list.pop();

		if self.list.count(self.head_mod) > 1:
			self.collided_self = True;
		else:
			self.collided_self = False;
		
		
	def on_position(self, pos):
		"""Returns whether the snake is on a given tile"""
		return self.list.count(pos);

	def is_head(self, pos):
		if pos == self.head_mod:
			return True;
		return False;


	def grow(self, dir):
		"""grows the snake in the given direction from the tail of the snake"""
		pass;

