class Player:
	max_HP = 80
	moves_per_turn = 2
	
	def __init__(self, organism1, organism2, name):
		self.organism1 = organism1
		self.organism2 = organism2
		self.num_berries = None
		self.name = name
		self.curr_HP = self.max_HP
		self.myTurn = False
		self.moves = moves_per_turn
		
	def __str__(self):
		return f"{self.name} {str(self.organism1)} {str(self.organism2)}"
		
	
