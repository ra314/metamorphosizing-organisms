from random

class Game:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
	
	def randomise_arena(self):
		arena = random.choice('stadium', 'forest valley', 'abandoned town')
		if arena == 'stadium':
			self.player1.HP = 60
			self.player2.HP = 60
		elif arena == 'forest valley':
			
		elif arena == 'abandoned town':
			
