import random
from Grid import Grid
from Drawable import Drawable
from Player import Player

class Game(Drawable):
	# Height and width
	grid_size = (5, 7)

	def __init__(self, player1, player2):
		self._players = (player1, player2)
		self.curr_player = None
		self.next_player = None
		self.grid = Grid(self.grid_size)
		self.draw_buffer = []
		self._actions_buffer = []
		self._shuffle_water = False
		self._start()
		self.turn_end_events = []

	def draw(self):
		self.draw_buffer.append(
			f'{self._players[0].draw()} \n\n'
			f'{self._players[1].draw()} \n\n'
			f'{self.grid.draw()}')

	def _start(self):
		self._add_game_reference_to_objects()
		self._randomise_arena()
		self._select_first_player()

	def _add_game_reference_to_objects(self):
		for player in self._players:
			player.add_game_reference_to_objects(self)
		self.grid.add_game_reference_to_objects(self)

	def _randomise_arena(self):
		arenas = {'tranquil falls': "Tranquil Falls: Water tiles will be shuffled at the start of a player's turn",
			'stadium': "Stadium: No stage modifiers are present",
			'forest valley': "Forest Valley: 1 less Berry to evolve",
			'abandoned town': "Abandoned Town: Evolving restores 10 HP"}
		arena = random.choice(list(arenas.keys()))

		if arena == 'stadium':
			pass

		elif arena == 'forest valley':
			Player.berries_to_evolve -= 1

		elif arena == 'abandoned town':
			Player.HP_restored_on_evolution = 10
			
		elif arena == 'tranquil falls':
			self._shuffle_water = True

		self.draw_buffer.append(arenas[arena])
			
	def _select_first_player(self):
		players = list(self._players)
		random.shuffle(players)
		self.curr_player, self.next_player = players
		# Giving the first player the default number of moves
		self.curr_player.reset_moves()
		# Giving the second player extra HP
		self.next_player.curr_HP += 5
		self.draw_buffer.append(f'The first player is {self.curr_player}. \n'
			f'{self.next_player} gets + 5 HP.')

	def add_mana(self, matches_per_type):
		print(f"Giving {matches_per_type} to {self.curr_player._name}")
		self.curr_player.add_mana(matches_per_type)

	def request_move(self):
		# Add the always available swap action
		actions_str = ["Swap 2 tiles: (x1 y1 x2 y2)"]
		self._actions_buffer = [self._swap_tiles_in_grid]

		# Debug options
		debug = True
		if debug:
			for index, organism in enumerate(self.curr_player.organisms):
				actions_str.append(f"Give {organism} x mana")
				self._actions_buffer.append(organism.change_num_mana)
				if organism.evolution:
					actions_str.append(f"Evolve {organism}")
					self._actions_buffer.append(lambda index = index: self.curr_player.evolve_organism(index))
			actions_str.append("Do nothing")
			self._actions_buffer.append(lambda: None)

		# Getting and adding actions from the player
		player_actions_str, player_actions = self.curr_player.get_actions()
		actions_str.extend(player_actions_str)

		# Storing these actions temporarily
		self._actions_buffer.extend(player_actions)

		# Draw game and send available actions to server
		self.draw()
		return str(self.curr_player), actions_str

	def process_move(self, index, player_inputs):
		# Parsing the selected action
		action = self._actions_buffer[index]
		return_value = True
		if player_inputs:
			return_value = action(*player_inputs)
		else:
			action()
		# Checking for an incorrect swap
		if not return_value:
			if action.__name__ == "_swap_tiles_in_grid":
				print("Incorrect parameters for swap")
			return

		# Deleting the actions buffer
		self._actions_buffer = []

		# Activating abilities
		for player in self._players:
			for organism in player.organisms:
				if organism.num_mana >= organism.mana_to_activate_ability:
					organism.num_mana = 0
					organism.ability()

		# Moving to the next player if necessary
		self.curr_player.moves -= 1
		if self.curr_player.moves == 0:
			self.next_player.reset_moves()
			self.curr_player, self.next_player = self.next_player, self.curr_player

			# Running turn end events
			print(self.turn_end_events)
			for event in self.turn_end_events:
				event.act()

			# Removing unsubscribed turn end events
			self.turn_end_events = [event for event in self.turn_end_events if event.subscribed]
			
			# Shuffling water tiles at start of turn
			if self._shuffle_water:
				self._shuffle_water_tiles()

	def _shuffle_water_tiles(self):
		self.grid.shuffle_water_tiles()
		
	def _swap_tiles_in_grid(self, x1, y1, x2, y2):
		if abs(x1-x2) + abs(y1-y2) != 1:
			return False
		self.grid.swap(x1, y1, x2, y2)
		return True
