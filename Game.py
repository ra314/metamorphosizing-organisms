import random
import Organism
import Player
import numpy as np
from ManaType import mana_indexes 

class Game:
	#Height and width
	grid_size = (5,7)
	
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.grid = None
		self.matches = None
		self.matches_per_type = np.zeros(len(mana_indexes))
		
	def display(self)
		return player1.display() + '\n'\
			player2.display() + '\n'\
			str(grid)
	
	def randomise_arena(self):
		arena = random.choice(['stadium', 'forest valley', 'abandoned town'])
		if arena == 'stadium':
			player.max_HP = 60
			player1.curr_HP = 60
			player2.curr_HP = 60
			
		elif arena == 'forest valley':
			Organism.berries_to_evolve = 3
			
		elif arena == 'abandoned town':
			Organism.HP_restored_on_evolution = 10
			
	def select_first_player(self):
		first_player = random.choice([self.player1, self.player2])
		first_player.my_turn = True
		first_player.curr_HP += 5
		
	def generate_tiles(self):
		self.grid = np.random.randint(0, len(mana_indexes), self.grid_size)
		
	def find_matches_in_grid(self):
		self.matches = np.zeros(self.grid_size)
		
		def match_tile(y,x):
			curr_tile = self.grid[y,x]
			
			#Check for matches above the curr tile
			if y-2 >= 0:
				if self.grid[y-1][x] == curr_tile and \
					self.grid[y-2][x] == curr_tile:
					self.matches[y,x] = 1
					self.matches[y-1,x] = 1
					self.matches[y-2,x] = 1
			
			#Check for matches to the left of the curr tile
			if x-2 >= 0:
				if self.grid[y][x-1] == curr_tile and \
					self.grid[y][x-2] == curr_tile:
					self.matches[y,x] = 1
					self.matches[y,x-1] = 1
					self.matches[y,x-2] = 1
		
		#Check for matches at each tile		
		for y in range(self.grid_size[0]):
			for x in range(self.grid_size[1]):
				match_tile(y,x)
					
	def find_and_remove_matched_tiles(self):
		for y in range(self.grid_size[0]):
			for x in range(self.grid_size[1]):
				if self.matches[y,x]:
					#Count the number of matches for each tile type
					self.matches_per_type[self.grid[y,x]] += 1
					#Mark tiles as removed
					self.grid[y,x] = -1
					
	def shift_tiles_down(self):
		for y in range(self.grid_size[0]):
			for x in range(self.grid_size[1]):
				#If the current tile is matched, pull down the closest unmatched tile above
				if self.grid[y,x] == -1:
					temp_y = y-1
					while temp_y >= 0 and self.grid[temp_y,x] == -1:
						temp_y -= 1
					if temp_y >= 0:
						self.grid[y,x] = self.grid[temp_y,x]
						self.grid[temp_y,x] = -1
	
	def fill_matched_tiles(self):
		for y in range(self.grid_size[0]):
			for x in range(self.grid_size[1]):
				#If the tile is matched, generate a random one
				if self.grid[y,x] == -1:
					self.grid[y,x] = random.randint(0, len(mana_indexes))
			
	
