class Organism:			
	def __init__(self, name, ability, mana_type, evolution):
		self.name = name
		self.ability = ability
		self.mana_type = mana_type
		self.num_mana = 0
		self.evolution = evolution
		
	def __str__(self):
		return self.name + '\n' + str(self.ability)
