import numpy as np
from ManaType import mana_indexes 

class Grid:	
	def __init__(self, size):
		self.grid = np.zeros(grid_size)
		self.matches = None
		self.matches_per_type = None
		self.display_buffer = []
		
	def __str__(self):
		return self.grid
		
	def add_grid_to_buffer(self):
		self.display_buffer.append(str(self.grid) + '\n'\
			+ str(self.matches_per_type))
		
	def initialize_grid(self):
		self.generate_tiles()
		self.initialize_matches_per_type()
		while True:
			if not self.find_matches_in_grid():
				break
			self.generate_tiles()
		self.add_grid_to_buffer()
	
	def initialize_matches_per_type(self)
		self.matches_per_type = np.zeros(len(mana_indexes))
		
	def match_grid(self):
		self.initialize_matches_per_type()
		while self.find_matches_in_grid():
			self.find_and_remove_matches_tiles()
			self.add_grid_to_buffer()
			self.shift_tiles_down()
			self.add_grid_to_buffer()
			self.fill_matched_tiles()
			self.add_grid_to_buffer()
		return self.matches_per_type
		
	def generate_tiles(self):
		self.grid = np.random.randint(0, len(mana_indexes), self.grid.shape)
		
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
				
		return np.sum(self.matches)
				
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
