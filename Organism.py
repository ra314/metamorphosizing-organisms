class Organism:
	def __init__(self, name, ability, mana_type_index, evolution):
		self.name = name
		self.ability = ability
		self.mana_type_index = mana_type_index
		self.mana_type = mana_types[mana_type_index]
		self._num_mana = 0
		self.evolution = evolution

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
		def clamp(lower_bound, x, upper_bound):
			if x > upper_bound:
				return upper_bound
			elif x < lower_bound:
				return lower_bound
			else:
				return x
		overflow_or_underflow_amount = (self._num_mana + delta) % self.ability.num_mana_to_activate
		self._num_mana = clamp(0, delta+self._num_mana, self.ability.num_mana_to_activate)
		return overflow_or_underflow_amount

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
