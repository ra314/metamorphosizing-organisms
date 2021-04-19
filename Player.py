class Player:
	max_HP = 80
	moves_per_turn = 2
	berries_to_evolve = 4
	HP_restored_on_evolution = 0

	def __init__(self, organism1, organism2, name):
		self._organisms = (organism1, organism2)
		self._num_berries = None
		self._name = name
		self.curr_HP = self.max_HP
		self.moves = 0

	def __str__(self):
		return self._name

	def display(self):
		HP_str = ('+' * int(self.curr_HP/5)) + ('-' * int((self.max_HP - self.curr_HP)/5))
		return f"{self._name} \n" \
			f"HP: {HP_str} \n" \
			f"{self._organisms[0].display()} \n" \
			f"{self._organisms[1].display()}"

	def get_actions(self):
		actions_str = []
		actions = []
		# Add evolution and boost actions where appropriate if the player has enough berries
		if self._num_berries == self.berries_to_evolve:
			for index, organism in enumerate(self._organisms):
				if organism.evolution:
					actions_str.append(f"Evolve {organism.name}")
					actions.append(lambda : self.evolve_organism(index))
				else:
					actions_str.append(f"Boost {organism.name}")
					actions.append(lambda : self.boost_organism(index))
		return actions_str, actions

	def change_HP(self, delta):
		self.curr_HP = max((delta + self.curr_HP), self.max_HP)

	def change_num_berries(self, delta):
		self._num_berries = max((delta + self._num_berries), self.berries_to_evolve)

	def evolve_organism(self, organism_index):
		self.change_HP(self.HP_restored_on_evolution)
		self._organisms[organism_index].evolve()

	def boost_organism(self, organism_index):
		self._organisms[organism_index].change_num_mana(self._num_berries)
		
	def reset_moves(self):
		self.moves = self.moves_per_turn
		
	def add_mana(self, matches_per_type):
		for organism in self._organisms:
			mana_gained = matches_per_type[organism.mana_type_index]
			organism.change_num_mana(mana_gained)