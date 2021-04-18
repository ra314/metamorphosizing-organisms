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
		HP_str = ('+' * self.curr_HP) + ('-' * (self.max_HP - self.curr_HP))
		return f"{self.name} \n" \
			f"HP: {HP_str} \n" \
			f"{self.organisms[0].display()} \n" \
			f"{self.organisms[1].display()}"

	def get_actions(self):
		actions_str = []
		actions = []
		if self.num_berries == self.berries_to_evolve:
			for index, organism in enumerate(self.organisms):
				if organism.evolution:
					actions_str.append(f"Evolve {organism.name}")
					actions.append(lambda : self.evolve_organism(index))
				else:
					actions_str.append(f"Boost {organism.name}")
					actions.append(lambda : self.boost_organism(index))
		return actions_str, actions

	def change_HP(self, delta):
		self.curr_HP = (delta + self.curr_HP) % self.max_HP

	def change_num_berries(self, delta):
		self.num_berries = (delta + self.num_berries) % self.berries_to_evolve

	def evolve_organism(self, organism_index):
		self.change_HP(self.HP_restored_on_evolution)
		self.organisms[organism_index].evolve()

	def boost_organism(self, organism_index):
		self.organisms[organism_index].change_num_mana(self.num_berries)
