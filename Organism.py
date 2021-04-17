class Organism:
	def __init__(self, name, ability, mana_type, evolution):
		self.name = name
		self.ability = ability
		self.mana_type = mana_type
		self.num_mana = 0
		self.evolution = evolution
		
	def __str__(self):
		return self.name
		
	def display(self):
		mana_str = ('+' * self.num_mana) + ('-' * (self.ability.num_mana_to_activate - self.num_mana))
		return self.name + '\n' + mana_str
		
	def evolve(self):
		self.name = self.evolution.name
		self.ability = self.evolution.ability
		self.evolution = None
		
	def change_num_mana(self, delta):
		self.num_mana = (delta + self.num_mana) % self.ability.num_mana_to_activate

from ManaType import mana_indexes
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
