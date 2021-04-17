import random
from queue import Queue
from Player import Player
from ManaType import mana_indexes 
from Grid import Grid

class Game:
	#Height and width
	grid_size = (5,7)
	
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.grid = Grid(self.grid_size)
		self.display_buffer = Queue()
		
	def display(self)
		return player1.display() + '\n'\
			player2.display() + '\n'\
			str(grid)
	
	def randomise_arena(self):
		arenas = {'stadium': "Stadium: Each player has 60 starting HP"
			'forest valley': "Forest Valley: 1 less Berry to evolve"
			'abandoned town': "Abandoned Town: Evolving restores 10 HP"}
		arena = random.choice(list(arenas.keys()))
		if arena == 'stadium':
			Player.max_HP = 60
			player1.curr_HP = 60
			player2.curr_HP = 60
			
		elif arena == 'forest valley':
			Player.berries_to_evolve -= 1
			
		elif arena == 'abandoned town':
			Player.HP_restored_on_evolution = 10
			
		return arenas[arena]
			
	def select_first_player(self):
		first_player, second_player = random.shuffle([self.player1, self.player2])
		first_player.my_turn = True
		second_player.curr_HP += 5
		return f"The first player is {first_player.name}. \n\
			{second_player}.name gets + 5 HP."
