import numpy as np
from ManaType import mana_indexes, mana_colors
from Drawable import Drawable


class Grid(Drawable):
	def __init__(self, grid_size):
		self._grid = np.zeros(grid_size)
		self._matches = None
		self._matches_per_type = None
		self._game = None
		self._initialize_grid()

	def __str__(self):
		output = ""
		for row in self._grid:
			for tile in row:
				if tile == -1:
					output +=  f"\u001b[36m#\u001b[0m"
				else:
					output += f"{mana_colors[tile]}{tile}"
			output += "\n"
		output += "\u001b[0m"
		return output

	def draw(self):
		return (
			f"Grid: \n"
			f"{self} \n"
			f"Matches made: \n"
			f"{' '.join([mana_colors[num]+str(num) for num in np.arange(len(self._matches_per_type))])} \u001b[0m \n"
			f"{' '.join([str(num) for num in self._matches_per_type])}")

	def _initialize_grid(self):
		self._generate_tiles()
		self._initialize_matches_per_type()
		# Ensuring there are no matches in the generated grid
		while True:
			if not self._find_matches_in_grid():
				break
			self._generate_tiles()

	def _generate_tiles(self):
		self._grid = np.random.randint(0, len(mana_indexes), self._grid.shape)

	def _initialize_matches_per_type(self):
		self._matches_per_type = np.zeros(len(mana_indexes)).astype('int')

	def _match_grid(self):
		while self._find_matches_in_grid():
			self._initialize_matches_per_type()
			self._check_for_extra_move()
			self._find_and_remove_matched_tiles()
			self._game.draw()

			self._game.add_mana(self._matches_per_type)
			self._initialize_matches_per_type()

			self._shift_tiles_down()
			self._game.draw()

			self._fill_matched_tiles()
			self._game.draw()

	def _find_matches_in_grid(self):
		self._matches = np.zeros(self._grid.shape)

		def match_tile_above_and_left(y, x):
			curr_tile = self._grid[y, x]

			# Check for matches above the curr tile
			if y - 2 >= 0:
				if self._grid[y - 1][x] == curr_tile and self._grid[y - 2][x] == curr_tile:
					self._matches[y, x] = 1
					self._matches[y - 1, x] = 1
					self._matches[y - 2, x] = 1

			# Check for matches to the left of the curr tile
			if x - 2 >= 0:
				if self._grid[y][x - 1] == curr_tile and self._grid[y][x - 2] == curr_tile:
					self._matches[y, x] = 1
					self._matches[y, x - 1] = 1
					self._matches[y, x - 2] = 1

		# Check for matches at each tile
		for y in range(self._grid.shape[0]):
			for x in range(self._grid.shape[1]):
				match_tile_above_and_left(y, x)

		# Returns if there are any matches or not
		return np.sum(self._matches) > 0

	def _check_for_extra_move(self):
		# Create a grid where the matched tiles retain their number and everything else is -1
		grid_with_only_matches = np.zeros(self._grid.shape) - 1
		for y in range(self._grid.shape[0]):
			for x in range(self._grid.shape[1]):
				if self._matches[y, x]:
					grid_with_only_matches[y, x] = self._grid[y, x]

		# Go through the grid with only matches and apply flood fill to find size of contiguous matches
		for y in range(self._grid.shape[0]):
			for x in range(self._grid.shape[1]):
				if grid_with_only_matches[y, x] != -1:
					match_size = self._flood_fill(grid_with_only_matches, y, x)
					if match_size > 3:
						self._game.curr_player.give_extra_move()

	def _flood_fill(self, grid, y, x):
		curr_tile = grid[y, x]
		queue = []
		match_size = 0

		def add_to_queue(y, x):
			nonlocal queue, match_size, grid
			if 0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]:
				if grid[y, x] == curr_tile:
					queue.append([y, x])
					grid[y, x] = -1
					match_size += 1

		# Performing flood fill
		add_to_queue(y, x)
		while queue:
			y, x = queue.pop()
			add_to_queue(y-1, x)
			add_to_queue(y+1, x)
			add_to_queue(y, x-1)
			add_to_queue(y, x+1)

		return match_size

	def _find_and_remove_matched_tiles(self):
		for y in range(self._grid.shape[0]):
			for x in range(self._grid.shape[1]):
				if self._matches[y, x]:
					# Count the number of matches for each tile type
					self._matches_per_type[self._grid[y, x]] += 1
					# Mark tiles as removed
					self._grid[y, x] = -1

	def _shift_tiles_down(self):
		tile_shifted = True
		while tile_shifted:
			tile_shifted = False
			for y in range(1, self._grid.shape[0]):
				for x in range(self._grid.shape[1]):
					# If the current tile is matched and the tile above isn't, swap them
					if self._grid[y, x] == -1 and self._grid[y-1, x] != -1 :
						self._grid[y, x], self._grid[y-1, x] = self._grid[y-1, x], self._grid[y, x]
						tile_shifted = True

	def _fill_matched_tiles(self):
		for y in range(self._grid.shape[0]):
			for x in range(self._grid.shape[1]):
				# If the tile is matched, generate a random one
				if self._grid[y, x] == -1:
					self._grid[y, x] = np.random.randint(0, len(mana_indexes))

	def swap(self, x1, y1, x2, y2):
		self._grid[y1, x1], self._grid[y2, x2] = self._grid[y2, x2], self._grid[y1, x1]
		self._game.draw()
		self._match_grid()

	def add_game_reference_to_objects(self, game):
		self._game = game

	def _shape_in_grid(self, tile_match_shape, y, x):
		# Start from the given seed and extend by the height and width of the shape
		# Check if these parts of the shape are also within the grid
		return y + tile_match_shape[0] <= self._grid.shape[0] and x + tile_match_shape[1] <= self._grid.shape[1]

	def _generate_random_coordinates(self):
		y = np.random.randint(self._grid.shape[0])
		x = np.random.randint(self._grid.shape[1])
		return y, x

	def force_grid_match(self, tile_match_shape):
		# tile_match_shape is a list of len 3. height, width and number of shapes

		# Replace -1s with height and width of grid
		if tile_match_shape[0] == -1:
			tile_match_shape[0] = self._grid.shape[0]
		if tile_match_shape[1] == -1:
			tile_match_shape[1] = self._grid.shape[1]

		while tile_match_shape[2]:
			# Pick a random tile and check that the shape is inside the grid
			while True:
				print("Finding a shape that is in the grid")
				seed_y, seed_x = self._generate_random_coordinates()
				print(f"seed y is {seed_y} and seed x is {seed_x}")
				if self._shape_in_grid(tile_match_shape, seed_y, seed_x):
					break

			print("Checking that the shape in the grid isn't already matched")
			# Checking that where the shape is placed does not interefe with already matched tiles
			for y in range(seed_y, seed_y + tile_match_shape[0]):
				for x in range(seed_x, seed_x + tile_match_shape[1]):
					if self._grid[y, x] == -1:
						continue

			# Mark those tiles as matched
			for y in range(seed_y, seed_y + tile_match_shape[0]):
				for x in range(seed_x, seed_x + tile_match_shape[1]):
					self._matches_per_type[self._grid[y, x]] += 1
					self._grid[y, x] = -1

			# This part of tile_match_shape represents how many duplicates of the shape should be found
			tile_match_shape[2] -= 1

		# Clearing the force matched grid and checking for more matches
		self._game.add_mana(self._matches_per_type)
		self._initialize_matches_per_type()

		self._shift_tiles_down()
		self._game.draw()

		self._fill_matched_tiles()
		self._game.draw()

		self._match_grid()

	def convert_tiles(self, tile_type, num_tiles):
		for i in range(num_tiles):
			# Pick a random tile and check that the type is different to the desired type
			while True:
				y, x = self._generate_random_coordinates()
				if self._grid[y, x] != tile_type:
					self._grid[y, x] = tile_type
					break

	def shuffle_water_tiles(self):
		water_tile_locations = self._grid == mana_indexes['water']
		for y1 in range(self._grid.shape[0]):
			for x1 in range(self._grid.shape[1]):
				if water_tile_locations[y1, x1]:
					while True:
						y2, x2 = self._generate_random_coordinates()
						if self._grid[y2, x2] != mana_indexes['water']:
							self._grid[y1, x1], self._grid[y2, x2] = self._grid[y2, x2], self._grid[y1, x1]
							break

		self._game.draw()
		self._match_grid()
