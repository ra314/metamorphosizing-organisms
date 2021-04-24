class Ability:
	def __init__(self, description, HP_delta, tile_match_shape, num_tiles_to_convert, increase_move_count,
				 num_berries_delta, num_mana_delta, num_mana_to_activate):
		# str
		self.description = description

		self.HP_delta = HP_delta
		"tuple of len 2. " \
		"(amount to increase player's HP, amount to increase opponent's HP)"

		self.tile_match_shape = tile_match_shape
		"tuple of len 3. " \
		"height, width and number of shapes"

		self.num_tiles_to_convert = num_tiles_to_convert

		self.increase_move_count = increase_move_count

		self.berries_delta = num_berries_delta
		"tuple of len 2. " \
		"(amount to increase player's berries, amount to increase opponent's berries)"

		self.mana_delta = num_mana_delta
		"tuple of len 4." \
		"(amount to increase player's 1st organism's mana, amount to increase player's 2nd organism's mana," \
		"amount to increase opponent's 1st organism's mana, amount to increase opponent's 2nd organism's mana)"

		self.num_mana_to_activate = num_mana_to_activate
		"amount of mana needed to activate ability"

	def __str__(self):
		return self.description

abilities = {}
abilities['Flare_plus'] = \
	Ability('Flare+: Attacks for 25 HP and matches 2 random columns.',
			(0, -25), (-1, 1, 2), 0, False, None, None, 8)
abilities['Flare'] = \
	Ability('Flare: Attacks for 20 HP and matches a random column.',
			(0, -20), (-1, 1, 1), 0, False, None, None, 8)

abilities['Hydro_Rush_plus'] = \
	Ability('Hydro Rush+: Attacks for 20 HP and converts 3 random tiles to Water.',
			(0, -20), None, 3, False, None, None, 6)
abilities['Hydro_Rush'] = \
	Ability('Hydro Rush: Attacks for 10 HP and converts 2 random tiles to Water.',
			(0, -10), None, 2, False, None, None, 6)

abilities['Heal_Leaf_plus'] = \
	Ability('Heal Leaf+: Attacks for 15HP and heals you for 15HP.',
			(15, -15), None, 0, False, None, None, 6)
abilities['Heal_Leaf'] = \
	Ability('Heal Leaf: Attacks for 10HP and heals you for 10HP.',
			(10, -10), None, 0, False, None, None, 6)
