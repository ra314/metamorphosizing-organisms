class Player:
	max_HP = 80
	moves_per_turn = 2
	berries_to_evolve = 4
	HP_restored_on_evolution = 0

	def __init__(self, organism1, organism2, name):
		self._organisms = (organism1, organism2)
		self._num_berries = 0
		self._name = name
		self.curr_HP = self.max_HP
		self.moves = 0
		self._game = None
		self._extra_move = False
		self._extra_move_on_next_turn = False

	def __str__(self):
		return self._name

	def draw(self):
		HP_str = ('+' * int(self.curr_HP/5)) + ('-' * int((self.max_HP - self.curr_HP)/5))
		berries_str = ('+' * self._num_berries) + ('-' * (self.berries_to_evolve - self._num_berries))
		return f"{self._name} \n" \
			f"HP: {HP_str} \n" \
			f"Berries (0): {berries_str} \n" \
			f"{self._organisms[0].draw()} \n" \
			f"{self._organisms[1].draw()}"

	def get_actions(self):
		actions_str = []
		actions = []
		# Add evolution and boost actions where appropriate if the player has enough berries
		if self._num_berries == self.berries_to_evolve:
			for index, organism in enumerate(self._organisms):
				if organism.evolution:
					actions_str.append(f"Evolve {organism.name}")
					actions.append(lambda: self.evolve_organism(index))
				else:
					actions_str.append(f"Boost {organism.name}")
					actions.append(lambda: self.boost_organism(index))
		return actions_str, actions

	def change_HP(self, delta):
		# Clamping HP
		self.curr_HP = min(max(0, delta+self.curr_HP), self.max_HP)
		self._game.draw()

	def change_num_berries(self, delta):
		# Clamping berries
		self._num_berries = min(max(0, delta+self._num_berries), self.berries_to_evolve)
		self._game.draw()

	def evolve_organism(self, organism_index):
		self.change_HP(self.HP_restored_on_evolution)
		self._organisms[organism_index].evolve()
		self._game.draw()

	def boost_organism(self, organism_index):
		self._organisms[organism_index].change_num_mana(self._num_berries)
		
	def reset_moves(self):
		self.moves = self.moves_per_turn
		if self.extra_move_on_next_turn:
			self.moves += 1
			self._extra_move_on_next_turn = False
			self._extra_move = True
		
	def add_mana(self, matches_per_type):
		print(matches_per_type)
		# Collecting berries
		self.change_num_berries(matches_per_type[0])
		# Distributing mana
		for organism in self._organisms:
			mana_gained = matches_per_type[organism.mana_type_index]
			mana_remaining = organism.change_num_mana(mana_gained)
			matches_per_type[organism.mana_type_index] = mana_remaining

	def add_game_reference_to_objects(self, game):
		self._game = game
		for organism in self._organisms:
			organism.add_game_reference_to_objects(game)
			
	def is_first_organism(self, organism):
		return self._organisms[0] == organism

	# Steal mana from the organism with the most and return the amount of mana stolen
	def steal_mana(self, mana_to_steal):
		selected_organism = max(self._organisms, key=lambda organism: organism.num_mana)
		mana_to_steal = min(selected_organism.num_mana, mana_to_steal)
		selected_organism.change_num_mana(-mana_to_steal)
		return mana_to_steal

	def give_extra_move(self, now):
		if now:
			if not self._extra_move:
				self._extra_move = True
				self.moves += 1
		else:
			self._extra_move_on_next_turn = True
