class Organism:			
	berries_to_evolve = 4
	HP_restored_on_evolution = 0
	
	def __init__(self, name, ability, mana_type, evolution):
		self.name = name
		self.ability = ability
		self.mana_type = mana_type
		self.num_mana = 0
		self.evolution = evolution
		
	def __str__(self):
		return self.name

from ManaType import mana_types
from Ability import abilities

stage_2_organisms = {}
stage_1_organisms = {}

stage_2_organisms['Bonzire'] = Organism('Bonzumi', abilities['Flare_plus'], 
	mana_types['fire'], None)
stage_1_organisms['Bonzumi'] = Organism('Bonzumi', abilities['Flare'], 
	mana_types['fire'], stage_2_organisms['Bonzire'])

stage_2_organisms['Sephanix'] = Organism('Sephanix', abilities['Hydro_Rush_plus'], 		
	mana_types['water'], None)
stage_1_organisms['Pelijet'] = Organism('Pelijet', abilities['Hydro_Rush'], 
	mana_types['water'], stage_2_organisms['Sephanix'])

stage_2_organisms['Karaggon'] = Organism('Karaggon', abilities['Heal_Leaf_plus'], 
	mana_types['grass'], None)
stage_1_organisms['Turtleisk'] = Organism('Turtleisk', abilities['Heal_Leaf'], 
	mana_types['grass'], stage_2_organisms['Karaggon'])
