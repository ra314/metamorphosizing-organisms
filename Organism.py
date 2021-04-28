class Organism:
	def __init__(self, name, ability, mana_type_index, evolution):
		self.name = name
		self.ability = ability
		self.mana_type_index = mana_type_index
		self.mana_type = mana_types[mana_type_index]
		self.num_mana = 0
		self.evolution = evolution
		self._game = None

	def __str__(self):
		return self.name

	def draw(self):
		mana_str = ('+' * self.num_mana) + ('-' * (self.ability.num_mana_to_activate - self.num_mana))
		return f"{self.name} ({self.mana_type_index}): {mana_str}"

	def evolve(self):
		# Retain mana type and and num_mana, mutate to evolved organism
		self.name = self.evolution.name
		self.ability = self.evolution.ability
		self.evolution = None

	def change_num_mana(self, delta):
		# Clamping mana
		prev_mana = self.num_mana
		self.num_mana = min(max(0, delta + self.num_mana), self.ability.num_mana_to_activate)
		# Checking for activated abilities
		if self.num_mana >= self.ability.num_mana_to_activate:
			self._game.activated_organisms.add(self)
		# Returning the amount of unused mana
		return abs(self.num_mana - prev_mana)

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
																					
stage_2_organisms['Axelraze'] = Organism('Axelraze', abilities['Electroclaw_plus'],
                                         mana_indexes['electric'], None)
stage_1_organisms['Slickitty'] = Organism('Slickitty', abilities['Electroclaw'],
                                          mana_indexes['electric'], stage_2_organisms['Axelraze'])

stage_2_organisms['Scoprikon'] = Organism('Scoprikon', abilities['Psycho_Bite_plus'],
                                         mana_indexes['psychic'], None)
stage_1_organisms['Barbenin'] = Organism('Barbenin', abilities['Psycho_Bite'],
                                          mana_indexes['psychic'], stage_2_organisms['Scoprikon'])
																						
stage_2_organisms['Magnooki'] = Organism('Magnooki', abilities['Pyro_Blitz_plus'],
                                         mana_indexes['fire'], None)
stage_1_organisms['Pyrokun'] = Organism('Pyrokun', abilities['Pyro_Blitz'],
                                          mana_indexes['fire'], stage_2_organisms['Magnooki'])
																						
stage_2_organisms['Shardivore'] = Organism('Shardivore', abilities['Aqua_Blast_plus'],
                                         mana_indexes['water'], None)
stage_1_organisms['Trashark'] = Organism('Trashark', abilities['Aqua_Blast'],
                                          mana_indexes['water'], stage_2_organisms['Shardivore'])

stage_2_organisms['Eidelf'] = Organism('Eidelf', abilities['Flower_Dance_plus'],
                                         mana_indexes['grass'], None)
stage_1_organisms['Elfini'] = Organism('Elfini', abilities['Flower_Dance'],
                                          mana_indexes['grass'], stage_2_organisms['Eidelf'])
																					
stage_2_organisms['Gleamur'] = Organism('Gleamur', abilities['Starblitz_plus'],
                                         mana_indexes['electric'], None)
stage_1_organisms['Winklit'] = Organism('Winklit', abilities['Starblitz'],
                                          mana_indexes['electric'], stage_2_organisms['Gleamur'])
																						
stage_2_organisms['Flambagant'] = Organism('Flambagant', abilities['Hugs_plus'],
                                         mana_indexes['fire'], None)
stage_1_organisms['Timingo'] = Organism('Timingo', abilities['Hugs'],
                                          mana_indexes['fire'], stage_2_organisms['Flambagant'])
																						
stage_2_organisms['Bandicrook'] = Organism('Bandicrook', abilities['Pickpocket_plus'],
                                         mana_indexes['psychic'], None)
stage_1_organisms['Criminook'] = Organism('Criminook', abilities['Pickpocket'],
                                          mana_indexes['psychic'], stage_2_organisms['Bandicrook'])
