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
		self.display_buffer = []
		self._actions = []
		self._start()

	def request_move(self):
		# Add the always available swap action
		actions_str = ["Swap 2 tiles: (x1 y1 x2 y2)"]
		self._actions = [lambda x1, y1, x2, y2: self._grid.swap(x1, y1, x2, y2)]
		
		# Getting and adding actions from the player
		player_actions_str, player_actions = self._curr_player.get_actions()
		actions_str.extend(player_actions_str)
		
		# Storing these actions temporarily
		self._actions.extend(player_actions)
		
		# Flushing the grid and game state so that player and grid info is still avaialble
		# Along with the enumerated actions at the bottom
		self._grid._flush_grid_to_buffer()
		self._flush_game_state_to_buffer()
		return str(self._curr_player), actions_str
		
	def process_move(self, index, additional_arguments):
		# Unwrapping extra arguments
		if additional_arguments:
			self._actions[index](*additional_arguments)
		else:
			self._actions[index]()
		self._actions = []
		
		# Moving to the next player
		self._curr_player.moves -= 1
		if self._curr_player.moves == 0:
			self._next_player.reset_moves()
			self._curr_player, self._next_player = self._next_player, self._curr_player
		
		self._flush_grid_updates_to_buffer()

	def _start(self):
		self._randomise_arena()
		self._select_first_player()
		self._flush_grid_updates_to_buffer()

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

		self.display_buffer.append(arenas[arena])
		
	def _flush_grid_updates_to_buffer(self):
		while self._grid.display_buffer:
			self._flush_game_state_to_buffer()

	def _flush_game_state_to_buffer(self):
		self.display_buffer.append(f'{self._players[0].display()} \n\n'
			f'{self._players[1].display()} \n\n'
			f'{self._grid.display_buffer.pop(0)}')
			
	def _select_first_player(self):
		players = list(self._players)
		random.shuffle(players)
		self._curr_player, self._next_player = players
		# Giving the first player the default number of moves
		self._curr_player.reset_moves()
		# Giving the second player extra HP
		self._next_player.curr_HP += 5
		self.display_buffer.append(f'The first player is {self._curr_player}. \n'
			f'{self._next_player} gets + 5 HP.')
