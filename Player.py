from Drawable import Drawable


class Player(Drawable):
	max_HP = 80
	moves_per_turn = 2
	berries_to_evolve = 4
	HP_restored_on_evolution = 0

	def __init__(self, organism1, organism2, name):
		self.organisms = [organism1, organism2]
		self.num_berries = 0
		self._name = name
		self.curr_HP = self.max_HP
		self.moves = 0
		self._game = None
		self._extra_move = False

	def __str__(self):
		return self._name

	def draw(self):
		HP_str = ('+' * int(self.curr_HP/5)) + ('-' * int((self.max_HP - self.curr_HP)/5))
		berries_str = ('+' * self.num_berries) + ('-' * (self.berries_to_evolve - self.num_berries))
		return f"{self._name} \n" \
			f"HP: {HP_str} \n" \
			f"Berries (0): {berries_str} \n" \
			f"Moves Left: {self.moves} \n" \
			f"{self.organisms[0].draw()} \n" \
			f"{self.organisms[1].draw()}"

	def get_actions(self):
		actions_str = []
		actions = []
		# Add evolution and boost actions where appropriate if the player has enough berries
		if self.num_berries == self.berries_to_evolve:
			for index, organism in enumerate(self.organisms):
				if organism.evolution:
					actions_str.append(f"Evolve {organism.name}")
					actions.append(lambda index = index: self.evolve_organism(index))
				else:
					actions_str.append(f"Boost {organism.name}")
					actions.append(lambda: self.boost_organism(index))
		return actions_str, actions

	def change_HP(self, delta):
		# Clamping HP
		# The max of current and max hp is done in the case of the start where p2 has 5 extra HP
		self.curr_HP = min(max(0, delta+self.curr_HP), max(self.curr_HP, self.max_HP))
		self._game.draw()

	def change_num_berries(self, delta):
		# Clamping berries
		self.num_berries = min(max(0, delta+self.num_berries), self.berries_to_evolve)
		self._game.draw()

	def evolve_organism(self, organism_index):
		self.change_HP(self.HP_restored_on_evolution)
		self.organisms[organism_index] = self.organisms[organism_index].evolve()
		self._game.draw()
		self.num_berries = 0

	def boost_organism(self, organism_index):
		self.organisms[organism_index].change_num_mana(self.num_berries)
		self.num_berries = 0
		
	def reset_moves(self):
		# Preventing a move underflow
		self.moves = max(0, self.moves + 2)
		self._extra_move = False
		
	def add_mana(self, matches_per_type):
		# Collecting berries
		self.change_num_berries(matches_per_type[0])
		# Distributing mana
		for organism in self.organisms:
			mana_gained = matches_per_type[organism.mana_type_index]
			mana_remaining = organism.change_num_mana(mana_gained)
			matches_per_type[organism.mana_type_index] = mana_remaining

	def add_game_reference_to_objects(self, game):
		self._game = game
		for organism in self.organisms:
			organism.add_game_reference_to_objects(game)

	def give_extra_move(self):
		if not self._extra_move:
			self._extra_move = True
			self.moves += 1
