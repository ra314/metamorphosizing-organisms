import Ability

class Organism:
	mana_types = ('fire', 'electric', 'water', 'grass')
	stage_1_organisms = initialize_organisms()
	
	def initialize_organisms():
		Flare_plus = Ability('Flare+: Attacks for 25 HP and matches 2 random columns.', (0,5), ((1,-1),(1,-1)), 0, False, None, None)
		Flare = Ability('Flare: Attacks for 20 HP and matches a random column.', (0,20), ((1,-1)), 0, False, None, None)
		Bonzire = Organism('Bonzumi', Flare_plus, 'fire', 8, None)
		Bonzumi = Organism('Bonzumi', Flare, 'fire', 8, Bonzire)

		Hydro_Rush_plus = Ability('Hydro Rush+: Attacks for 20 HP and converts 23random tiles to Water.', (0,20), None, 3, False, None, None)
		Hydro_Rush = Ability('Hydro Rush: Attacks for 10 HP and converts 2 random tiles to Water.', (0,10), None, 2, False, None, None)
		Sephanix = Organism('Sephanix', Hydro_Rush_plus, 'water', 6, None)
		Pelijet = Organism('Pelijet', Hydro_Rush, 'water', 6, Sephanix)

		Heal_Leaf_plus = Ability('Heal Leaf+: Attacks for 15HP and heals you for 15HP.', (10,10), None, 0, False, None, None)
		Heal_Leaf = Ability('Heal Leaf: Attacks for 10HP and heals you for 10HP.', (10,10), None, 0, False, None, None)
		Karaggon = Organism('Karaggon', Heal_Leaf_plus, 'grass', 6, None)
		Turtleisk = Organism('Turtleisk', Heal_Leaf, 'grass', 6, Karaggon)
		
		return (Bonzumi, Pelijet, Turtleisk)
			
	def __init__(self, name, ability, mana_type, evolution):
		self.name = name
		self.ability = ability
		self.mana_type = mana_type
		self.num_mana = 0
		self.evolution = evolution
		
	def __str__(self):
		return self.name + \n + self.ability.getDescription()
