class Player:
	max_HP = 80
	moves_per_turn = 2
	berries_to_evolve = 4
	HP_restored_on_evolution = 0
	
	def __init__(self, organism1, organism2, name):
		self.organisms = (organism1, organism2)
		self.num_berries = None
		self.name = name
		self.curr_HP = self.max_HP
		self.moves = self.moves_per_turn
		
	def __str__(self):
		return self.name
		
	def display(self):
		return self.name + '\n'\
			+ self.organisms[0].display() + '\n'\
			+ self.organisms[1].display()
			
	def get_actions(self):
		actions = ["Swap 2 tiles"]
		if self.num_berries == self.berries_to_evolve:
			for organism in self.organisms:
				if organism.evolution:
					actions.append(f"Evolve {organism.name}")
				else:
					actions.append(f"Boost {organism.name}")
		return actions
		
	def change_HP(self, delta):
		self.curr_HP = (delta + self.curr_HP) % self.max_HP
		
	def change_num_berries(self, delta):
		self.num_berries = (delta + self.num_berries) % self.berries_to_evolve
		
	def evolve_organism(self, organism_index):
		self.change_HP(self.HP_restored_on_evolution)
		self.organisms[organism_index].evolve()
		
	def boost_organism(self, organism_index):
		self.organisms[organism_index].change_num_mana(self.num_berries)
