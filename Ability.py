class Ability:
	def __init__(self, description, HP_delta, tile_match_shape, num_tiles_to_convert, increase_move_count, num_berries_delta, num_mana_delta, num_mana_to_activate):
		#str
		self.description = description
		
		#tuple of len 2. (amount to increase player's HP, amount to decrease opponent's HP)
		self.HP_delta = HP_delta
		
		#list. contains tuples which contains x and y coordinates of the shapes to match.
		self.tile_match_shape = tile_match_shape
		
		self.num_tiles_to_convert = num_tiles_to_convert
		
		self.increase_move_count = increase_move_count
		
		#tuple of len 2. (amount to increase player's berries, amount to decrease opponent's berries)
		self.num_berries_delta = num_berries_delta
		
		#tuple of len 4. 
		#(amount to increase player's 1st organism's mana, amount to increase player's 2nd organism's mana,
		#amount to decrease opponent's 1st organism's mana, amount to decrease opponent's 2nd organism's mana)
		self.num_mana_delta = num_mana_delta
		
		#amount of mana needed to activate ability
		self.num_mana_to_activate = num_mana_to_activate
		
	def get_description(self):
		return self.description
