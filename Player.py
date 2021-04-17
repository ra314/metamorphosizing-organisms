class Player:
	def __init__(self, organism1, organism2, HP, name):
		self.organism1 = organism1
		self.organism2 = organism2
		self.HP = HP
		self.num_berries = 0
		self.name = name
		
	def __str__(self):
		return f"{self.name} {str(self.organism1)} {str(self.organism2)}"
