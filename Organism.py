class Organism:
	def __init__(self, name, ability, mana_type_index, evolution):
		self.name = name
		self.ability = ability
		self.mana_type_index = mana_type_index
		self.mana_type = mana_types[mana_type_index]
		self._num_mana = 0
		self.evolution = evolution
		self._game = None

	def __str__(self):
		return self.name

	def display(self):
		mana_str = ('+' * self._num_mana) + ('-' * (self.ability.num_mana_to_activate - self._num_mana))
		return f"{self.name} \n" \
            f"{self.mana_type} ({self.mana_type_index}): {mana_str}"

	def evolve(self):
		# Retain mana type and and num_mana, mutate to evolved organism
		self.name = self.evolution.name
		self.ability = self.evolution.ability
		self.evolution = None

	def change_num_mana(self, delta):
		# Clamping mana
		prev_mana = self._num_mana
		self._num_mana = min(max(0, delta+self._num_mana), self.ability.num_mana_to_activate)
		# Checking for activated abilities
		if self._num_mana >= self.ability.num_mana_to_activate:
			self._game.activated_organisms.add(self)
		# Returning the amount of unused mana
		return abs(self._num_mana - prev_mana)

	def add_game_reference_to_objects(self, game):
		self._game = game

from ManaType import mana_indexes, mana_types
from Ability import abilities

stage_2_organisms = {}
stage_1_organisms = {}

stage_2_organisms['Bonzire'] = Organism('Bonzumi', abilities['Flare_plus'],
                                        mana_indexes['fire'], None)
stage_1_organisms['Bonzumi'] = Organism('Bonzumi', abilities['Flare'],
                                        mana_indexes['fire'], stage_2_organisms['Bonzire'])

stage_2_organisms['Sephanix'] = Organism('Sephanix', abilities['Hydro_Rush_plus'],
                                         mana_indexes['water'], None)
stage_1_organisms['Pelijet'] = Organism('Pelijet', abilities['Hydro_Rush'],
                                        mana_indexes['water'], stage_2_organisms['Sephanix'])

stage_2_organisms['Karaggon'] = Organism('Karaggon', abilities['Heal_Leaf_plus'],
                                         mana_indexes['grass'], None)
stage_1_organisms['Turtleisk'] = Organism('Turtleisk', abilities['Heal_Leaf'],
                                          mana_indexes['grass'], stage_2_organisms['Karaggon'])
