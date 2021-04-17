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
			Player.max_HP = 60
			
		elif arena == 'forest valley':
			Organism.berries_to_evolve = 3
			
		elif arena == 'abandoned town':
			Organism.HP_restored_on_evolution = 10
