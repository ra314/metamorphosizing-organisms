class Ability:
	def __init__(self, description, HP_delta, tile_match_shape, num_tiles_to_convert, mana_type, increase_move_count, num_berries_delta, num_mana_delta):
		#str
		self.description = description
		
		#list of len 2. [amount to increase player's HP, amount to decrease opponent's HP]
		self.HP_delta = HP_delta
		
		#list of len 2. x and y coordinates of shape.
		self.tile_match_shape = tile_match_shape
		
		self.num_tiles_to_convert = num_tiles_to_convert
		self.mana_type = mana_type
		
		self.increase_move_count = increase_move_count
		
		#list of len 2. [amount to increase player's berries, amount to decrease opponent's berries]
		self.num_berries_delta = num_berries_delta
		
		#list of len 4. 
		#[amount to increase player's 1st organism's mana, amount to increase player's 2nd organism's mana]
		#[amount to decrease opponent's 1st organism's mana, amount to decrease opponent's 2nd organism's mana]
		self.num_mana_delta = num_mana_delta
