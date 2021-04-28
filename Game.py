import random
from Player import Player
from Grid import Grid


class Game:
	# Height and width
	grid_size = (5, 7)

	def __init__(self, player1, player2):
		self._players = (player1, player2)
		self._curr_player = None
		self._next_player = None
		self._grid = Grid(self.grid_size)
		self.draw_buffer = []
		self.activated_organisms = set()
		self._actions_buffer = []
		self._start()

	def draw(self):
		self.draw_buffer.append(
			f'{self._players[0].draw()} \n\n'
			f'{self._players[1].draw()} \n\n'
			f'{self._grid.draw()}')

	def _start(self):
		self._add_game_reference_to_objects()
		self._randomise_arena()
		self._select_first_player()

	def _add_game_reference_to_objects(self):
		for player in self._players:
			player.add_game_reference_to_objects(self)
		self._grid.add_game_reference_to_objects(self)

	def _randomise_arena(self):
		arenas = {'stadium': "Stadium: Each player has 60 starting HP",
			'forest valley': "Forest Valley: 1 less Berry to evolve",
			'abandoned town': "Abandoned Town: Evolving restores 10 HP"}
		arena = random.choice(list(arenas.keys()))

		if arena == 'stadium':
			Player.max_HP = 60
			# noinspection PyPep8Naming
			self._players[0].curr_HP = 60
			# noinspection PyPep8Naming
			self._players[1].curr_HP = 60

		elif arena == 'forest valley':
			Player.berries_to_evolve -= 1

		elif arena == 'abandoned town':
			Player.HP_restored_on_evolution = 10

		self.draw_buffer.append(arenas[arena])
			
	def _select_first_player(self):
		players = list(self._players)
		random.shuffle(players)
		self._curr_player, self._next_player = players
		# Giving the first player the default number of moves
		self._curr_player.reset_moves()
		# Giving the second player extra HP
		self._next_player.curr_HP += 5
		self.draw_buffer.append(f'The first player is {self._curr_player}. \n'
			f'{self._next_player} gets + 5 HP.')

	def add_mana(self, matches_per_type):
		self._curr_player.add_mana(matches_per_type)

	def request_move(self):
		# Add the always available swap action
		actions_str = ["Swap 2 tiles: (x1 y1 x2 y2)"]
		self._actions_buffer = [self._swap_tiles_in_grid]

		# Getting and adding actions from the player
		player_actions_str, player_actions = self._curr_player.get_actions()
		actions_str.extend(player_actions_str)

		# Storing these actions temporarily
		self._actions_buffer.extend(player_actions)

		# Draw game and send available actions to server
		self.draw()
		return str(self._curr_player), actions_str

	def process_move(self, index, player_inputs):
		# Parsing the selected action
		action = self._actions_buffer[index]
		if action.__name__ == "_swap_tiles_in_grid":
			action(*player_inputs)
		else:
			action()
		# Deleting the actions buffer
		self._actions_buffer = []

		# Activating abilities
		for organism in self.activated_organisms:
			self._process_ability(organism)

		# Moving to the next player if necessary
		self._curr_player.moves -= 1
		if self._curr_player.moves == 0:
			self._next_player.reset_moves()
			self._curr_player, self._next_player = self._next_player, self._curr_player

	def _swap_tiles_in_grid(self, x1, y1, x2, y2):
		self._grid.swap(x1, y1, x2, y2)
		
	def _process_ability(self, organism):
		# Changing HP
		if organism.ability.HP_delta:
			# Changing the order of the delta to align it with the inteded recipients
			HP_delta = organism.ability.HP_delta
			if not self._curr_player.is_first_organism(organism):
				HP_delta = [delta[::-1] for delta in HP_delta]
				
			self._curr_player.change_HP(HP_delta[0])
			self._next_player.change_HP(HP_delta[1])
			
		# Matching tiles in a specific shape
		if organism.ability.tile_match_shape:
			self._grid.force_grid_match(organism.ability.tile_match_shape)

		# Changing Mana
		if organism.ability.mana_delta:
			# Changing the order of the delta to align it with the inteded recipients
			mana_delta = organism.ability.HP_delta
			if not self._curr_player.is_first_organism(organism):
				mana_delta = [delta[::-1] for delta in mana_delta]

			self._curr_player.change_HP(mana_delta[0])
			self._next_player.change_HP(mana_delta[1])

		# Converting tiles
		if organism.ability.num_tiles_to_convert:
			self._grid.convert_tiles(organism.mana_type_index, organism.ability.num_tiles_to_convert)