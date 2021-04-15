class Organism:
	def __init__(self, name, ability, tile_type, num_tiles_to_activate):
		self.name = name
		self.ability = ability
		self.tile_type = tile_type
		self.num_tiles = 0
		self.num_tiles_to_activate = num_tiles_to_activate
