class Player:
	def __init__(self, organism1, organism2, name):
		self.organism1 = organism1
		self.organism2 = organism2
		self.HP = 60
		self.num_berries = None
		self.name = name
		
	def __str__(self):
		return f"{self.name} {str(self.organism1)} {str(self.organism2)}"
		
	
