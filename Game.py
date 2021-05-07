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
		self._shuffle_water = False
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
		arenas = {'tranquil falls': "Tranquil Falls: Water tiles will be shuffled at the start of a player's turn",
			'stadium': "Stadium: No stage modifiers are present",
			'forest valley': "Forest Valley: 1 less Berry to evolve",
			'abandoned town': "Abandoned Town: Evolving restores 10 HP"}
		arena = random.choice(list(arenas.keys()))

		arena = 'tranquil falls'

		if arena == 'stadium':
			pass

		elif arena == 'forest valley':
			Player.berries_to_evolve -= 1

		elif arena == 'abandoned town':
			Player.HP_restored_on_evolution = 10
			
		elif arena == 'tranquil falls':
			# Currently does nothing
			self._shuffle_water = True

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
		# Shuffling water tiles at start of turn
		if self._shuffle_water:
			self._shuffle_water_tiles()

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
			self.activated_organisms.remove(organism)
			self._process_ability(organism)

		# Moving to the next player if necessary
		self._curr_player.moves -= 1
		if self._curr_player.moves == 0:
			self._next_player.reset_moves()
			self._curr_player, self._next_player = self._next_player, self._curr_player

	def _shuffle_water_tiles(self):
		self._grid.shuffle_water_tiles()
		
	def _swap_tiles_in_grid(self, x1, y1, x2, y2):
		self._grid.swap(x1, y1, x2, y2)
		
	def _process_ability(self, organism):
		organism.num_mana = 0

		# Changing HP
		if organism.ability.HP_delta:
			# Checking for delayed HP Delta
			if organism.ability.HP_delta_duration:
				self._curr_player.add_delayed_HP_delta(organism, organism.ability.HP_delta[0], organism.ability.HP_delta_duration)
				self._next_player.add_delayed_HP_delta(organism, organism.ability.HP_delta[1], organism.ability.HP_delta_duration)
			else:
				self._curr_player.change_HP(organism.ability.HP_delta[0])
				self._next_player.change_HP(organism.ability.HP_delta[1])
			
		# Matching tiles in a specific shape
		if organism.ability.tile_match_shape:
			self._grid.force_grid_match(organism.ability.tile_match_shape)

		# Changing Mana
		if organism.ability.mana_delta:
			# Changing the order of the delta to align it with the intended recipients
			mana_delta = organism.ability.HP_delta
			if not self._curr_player.is_first_organism(organism):
				mana_delta = [mana_delta[1], mana_delta[0], mana_delta[3], mana_delta[2]]

			self._curr_player.change_mana(mana_delta[:int(len(mana_delta)/2)])
			self._next_player.change_mana(mana_delta[int(len(mana_delta)/2):])

		# Converting tiles
		if organism.ability.num_tiles_to_convert:
			self._grid.convert_tiles(organism.mana_type_index, organism.ability.num_tiles_to_convert)
		
		# Changing Berries
		if organism.ability.berries_to_steal:
			berries_to_steal = min(organism.ability.berries_to_steal, self._next_player.num_berries)
			# Steal the berries from the intended target
			self._curr_player.change_num_berries(berries_to_steal)
			self._next_player.change_num_berries(-berries_to_steal)

		# Stealing mana
		if organism.ability.mana_to_steal:
			# Steal mana from the intended target
			mana_stolen = self._next_player.steal_mana(organism.ability.mana_to_steal)
			organism.change_num_mana(mana_stolen)

		# Increasing move count on next turn
		if organism.ability.move_bonus_delta:
			self._curr_player.change_num_moves(organism, organism.ability.move_bonus_delta, organism.ability.move_bonus_duration)

		self.draw()
