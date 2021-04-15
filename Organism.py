class Organism:
	def __init__(self, name, ability, mana_type, num_mana_to_activate):
		self.name = name
		self.ability = ability
		self.mana_type = mana_type
		self.num_mana = 0
		self.num_mana_to_activate = num_mana_to_activate
