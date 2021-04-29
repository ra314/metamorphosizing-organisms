class Ability:
    def __init__(self, description, HP_delta, num_mana_to_activate, tile_match_shape = None, HP_delta_duration = 0, num_tiles_to_convert = 0,
		move_bonus_delta = 0, move_bonus_duration = 0, berries_to_steal = 0, mana_to_steal = 0, mana_delta = None):
        # str
        self.description = description
				
        self.HP_delta = HP_delta
        "tuple of len 2. " \
        "(amount to increase player's HP, amount to increase opponent's HP)"
				
        self.num_mana_to_activate = num_mana_to_activate
        "amount of mana needed to activate ability"
				
        self.tile_match_shape = tile_match_shape
        "tuple of len 3. " \
        "height, width and number of shapes"				
				
        self.HP_delta_duration = HP_delta_duration
        "duration of the healing"
				
        self.num_tiles_to_convert = num_tiles_to_convert
				"amount of tiles this ability will convert" \
				"relative to the organism's mana type"
				
        self.move_bonus_delta = move_bonus_delta
        "amount of bonus moves this ability grants"
				
        self.move_bonus_duration = move_bonus_duration
        "duration (in turns) that the move bonus lasts for"
				
        self.berries_to_steal = berries_to_steal
				
        self.mana_to_steal = mana_to_steal
				
        self.mana_delta = mana_delta
        "tuple of len 4." \
        "(amount to increase casting organism's mana, amount to increase allied organism's mana," \
        "amount to increase organism's mana (opposite to casting organism), amount to increase opponent's allied organism's mana (adjacent to the opposite casting organism)"

    def __str__(self):
        return self.description


abilities = {}
abilities['Flare_plus'] = \
    Ability('Flare+: Attacks for 25 HP and matches 2 random columns.',
						(0, -25), 8, tile_match_shape = (-1, 1, 2))
abilities['Flare'] = \
    Ability('Flare+: Attacks for 25 HP and matches 2 random columns.',
						(0, -25), 8, tile_match_shape = (-1, 1, 1))

abilities['Hydro_Rush_plus'] = \
    Ability('Hydro Rush+: Attacks for 20 HP and converts 3 random tiles to Water.',
            (0, -20), 6, num_tiles_to_convert = 3)
abilities['Hydro_Rush'] = \
    Ability('Hydro Rush: Attacks for 10 HP and converts 2 random tiles to Water.',
            (0, -10), 6, num_tiles_to_convert = 2)

abilities['Heal_Leaf_plus'] = \
    Ability('Heal Leaf+: Attacks for 15 HP and heals you for 15 HP.',
            (15, -15), 6)
abilities['Heal_Leaf'] = \
    Ability('Heal Leaf: Attacks for 10 HP and heals you for 10 HP.',
            (10, -10), 6)

abilities['Electroclaw_plus'] = \
    Ability('Electroclaw+: Attacks for 10 HP and matches a random 3x2 grid.',
            (0, -10), 4, tile_match_shape = (2, 3, 1))
abilities['Electroclaw'] = \
    Ability('Electroclaw: Attacks for 5 HP and matches a random 2x2 grid.',
            (0, -5), 4, tile_match_shape = (2, 2, 1))

abilities['Psycho_Bite_plus'] = \
    Ability("Psycho Bite+: Attacks for 15 HP and drains 3 Mana from opponent's monsters.",
            (0, -15), 6, mana_delta = (0, 0, -3, -3))
abilities['Psycho_Bite'] = \
    Ability("Psycho Bite: Attacks for 10 HP and drains 2 Mana from opponent's monsters.",
            (0, -10), 6, mana_delta = (0, 0, -2, -2))

abilities['Pyro_Blitz_plus'] = \
    Ability('Pyro Blitz+: Attacks for 35 HP and matches a random row.',
            (0, -35), 10, tile_match_shape = (1, -1, 1))
abilities['Pyro_Blitz'] = \
    Ability('Pyro Blitz: Attacks for 25 HP and matches a random row.',
            (0, -25), 10, tile_match_shape = (1, -1, 1))

abilities['Aqua_Blast_plus'] = \
    Ability('Aqua Blast+: Attacks for 25 HP and converts 3 random tiles to Water.',
            (0, -35), 10, num_tiles_to_convert = 3)
abilities['Aqua_Blast'] = \
    Ability('Aqua Blast: Attacks for 20 HP and converts 2 random tiles to Water.',
            (0, -25), 10, num_tiles_to_convert = 2)

abilities['Flower_Dance_plus'] = \
    Ability('Flower Dance+: Attacks for 10 HP and heals 10 HP at the end of the turn for two turns.',
            (10, -10), 6, HP_delta_duration = 2)
abilities['Flower_Dance'] = \
    Ability('Flower Dance: Attacks for 5 HP and heals 5 HP at the end of the turn for two turns.',
            (5, -5), 6, HP_delta_duration = 2)

abilities['Starblitz_plus'] = \
    Ability('Starblitz+: Attacks for 15 HP and grants 1 extra move in the next turn.',
            (0, -15), 6, move_bonus_delta = 1, move_bonus_duration = 1)
abilities['Starblitz'] = \
    Ability('Starblitz: Attacks for 10 HP and grants 1 extra move in the next turn.',
            (0, -10), 6, move_bonus_delta = 1, move_bonus_duration = 1)

abilities['Hugs_plus'] = \
    Ability('Hugs+: Attacks for 15 HP and gives 3 mana to your other monster.',
            (0, -15), 6, mana_delta = (0, 3, 0, 0))
abilities['Hugs'] = \
    Ability('Hugs: Attacks for 10 HP and gives 2 mana to your other monster.',
            (0, -10), 6, mana_delta = (0, 3, 0, 0))

abilities['Pickpocket_plus'] = \
    Ability('Pickpocket+: Attacks for 10 HP and steals up to 2 berries and 2 mana.',
            (0, -10), 6, berries_to_steal = 2, mana_to_steal = 2, mana_delta = (0, 0, -3, 0))
abilities['Pickpocket'] = \
    Ability('Pickpocket: Attacks for 10 HP and steals up to 2 berries and 1 mana.',
            (0, -10), 6, berries_to_steal = 2, mana_to_steal = 1, mana_delta = (0, 0, -2, 0))

abilities['Punish_plus'] = \
    Ability('Punish+: Attacks for 45 HP but loses 1 move for the next 2 turns.',
            (0, -45), 10, move_bonus_delta = -1, move_bonus_duration = 2)
abilities['Punish'] = \
    Ability('Punish: Attacks for 35 HP but loses 1 move for the next 1 turn.',
            (0, -35), 10, move_bonus_delta = -1, move_bonus_duration = 1)
