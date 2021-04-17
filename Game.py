import random
import Organism
import Player

class Game:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
	
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
		first_player.myTurn = True
		first_player.curr_HP += 5
