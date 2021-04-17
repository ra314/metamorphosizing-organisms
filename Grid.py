import numpy as np
from ManaType import mana_indexes


class Grid:
    def __init__(self, grid_size):
        self._grid = np.zeros(grid_size)
        self._matches = None
        self._matches_per_type = None
        self.display_buffer = []
        self._initialize_grid()

    def __str__(self):
        return str(self._grid)

    def _update_buffer(self):
        self.display_buffer.append(str(self._grid) + '\n' \
                                   + str(self._matches_per_type))

    def _initialize_grid(self):
        self._generate_tiles()
        self._initialize_matches_per_type()
        while True:
            if not self._find_matches_in_grid():
                break
            self._generate_tiles()
        self._update_buffer()

    def _generate_tiles(self):
        self._grid = np.random.randint(0, len(mana_indexes), self._grid.shape)

    def _initialize_matches_per_type(self):
        self._matches_per_type = np.zeros(len(mana_indexes))

    def match_grid(self):
        self._initialize_matches_per_type()
        while self._find_matches_in_grid():
            self._find_and_remove_matched_tiles()
            self._update_buffer()
            self._shift_tiles_down()
            self._update_buffer()
            self._fill_matched_tiles()
            self._update_buffer()
        return self._matches_per_type

    def _find_matches_in_grid(self):
        self._matches = np.zeros(self._grid.shape)

        def match_tile(y, x):
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
                match_tile(y, x)

        return np.sum(self._matches)

    def _find_and_remove_matched_tiles(self):
        for y in range(self._grid.shape[0]):
            for x in range(self._grid.shape[1]):
                if self._matches[y, x]:
                    # Count the number of matches for each tile type
                    self._matches_per_type[self._grid[y, x]] += 1
                    # Mark tiles as removed
                    self._grid[y, x] = -1

    def _shift_tiles_down(self):
        for y in range(self._grid.shape[0]):
            for x in range(self._grid.shape[1]):
                # If the current tile is matched, pull down the closest unmatched tile above
                if self._grid[y, x] == -1:
                    temp_y = y - 1
                    while temp_y >= 0 and self._grid[temp_y, x] == -1:
                        temp_y -= 1
                    if temp_y >= 0:
                        self._grid[y, x] = self._grid[temp_y, x]
                        self._grid[temp_y, x] = -1

    def _fill_matched_tiles(self):
        for y in range(self._grid.shape[0]):
            for x in range(self._grid.shape[1]):
                # If the tile is matched, generate a random one
                if self._grid[y, x] == -1:
                    self._grid[y, x] = np.random.randint(0, len(mana_indexes))
