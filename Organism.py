from abc import ABC, abstractmethod
from ManaType import mana_indexes, mana_types, mana_colors
from Drawable import Drawable


class Organism(Drawable, ABC):
	def __init__(self, name, ability_description, mana_to_activate_ability, mana_type_index, evolution):
		self.name = name
		self.ability_description = ability_description
		self.mana_to_activate_ability = mana_to_activate_ability
		self.mana_type_index = mana_type_index
		self.mana_type = mana_types[mana_type_index]
		self.num_mana = 0
		self.evolution = evolution
		self.game = None

	def __str__(self):
		return self.name

	def draw(self):
		mana_str = ('+' * self.num_mana) + ('-' * (self.mana_to_activate_ability - self.num_mana))
		return f"{mana_colors[self.mana_type_index]}{self.name} ({self.mana_type_index}): {mana_str} \u001b[0m"

	def evolve(self):
		evolved_organism = self.evolution()
		evolved_organism.num_mana = self.num_mana
		evolved_organism.game = self.game
		return evolved_organism

	@abstractmethod
	def ability(self):
		pass

	def change_num_mana(self, delta):
		# Clamping mana
		prev_mana = self.num_mana
		self.num_mana = min(max(0, delta + self.num_mana), self.mana_to_activate_ability)

		# Returning the amount change in mana
		return abs(self.num_mana - prev_mana)

	def add_game_reference_to_objects(self, game):
		self.game = game


class Bonzire(Organism):
	def __init__(self):
		super().__init__("Bonzire", 'Flare+: Attacks for 25 HP and matches 2 random columns.', 8, mana_indexes['fire'], None)

	def ability(self):
		self.game.next_player.change_HP(-25)
		self.game.grid.force_grid_match([-1, 1, 2])


class Bonzumi(Organism):
	def __init__(self):
		super().__init__("Bonzumi", 'Flare: Attacks for 20 HP and matches 1 random columns.', 8, mana_indexes['fire'], Bonzire)

	def ability(self):
		self.game.next_player.change_HP(-20)
		self.game.grid.force_grid_match([-1, 1, 1])


class Sephanix(Organism):
	def __init__(self):
		super().__init__("Sephanix", 'Hydro Rush+: Attacks for 20 HP and converts 3 random tiles to Water.', 6, mana_indexes['water'], None)

	def ability(self):
		self.game.next_player.change_HP(-20)
		self.game.grid.convert_tiles(self.mana_type_index, 3)


class Pelijet(Organism):
	def __init__(self):
		super().__init__("Pelijet", 'Hydro Rush: Attacks for 10 HP and converts 2 random tiles to Water.', 6, mana_indexes['water'], Sephanix)

	def ability(self):
		self.game.next_player.change_HP(-10)
		self.game.grid.convert_tiles(self.mana_type_index, 2)


class Karaggon(Organism):
	def __init__(self):
		super().__init__("Karaggon", 'Heal Leaf+: Attacks for 15 HP and heals you for 15 HP.', 6, mana_indexes['grass'], None)

	def ability(self):
		self.game.next_player.change_HP(-15)
		self.game.curr_player.change_HP(15)


class Turtleisk(Organism):
	def __init__(self):
		super().__init__("Turtleisk", 'Heal Leaf: Attacks for 10 HP and heals you for 10 HP.', 6, mana_indexes['grass'], Karaggon)

	def ability(self):
		self.game.next_player.change_HP(-10)
		self.game.curr_player.change_HP(10)


class Axelraze(Organism):
	def __init__(self):
		super().__init__("Axelraze", 'Electroclaw+: Attacks for 10 HP and matches a random 3x2 grid.', 4, mana_indexes['electric'], None)

	def ability(self):
		self.game.next_player.change_HP(-10)
		self.game.grid.force_grid_match([3, 2, 1])


class Slickitty(Organism):
	def __init__(self):
		super().__init__("Slickitty", 'Electroclaw: Attacks for 5 HP and matches a random 2x2 grid.', 4, mana_indexes['electric'], Axelraze)

	def ability(self):
		self.game.next_player.change_HP(-5)
		self.game.grid.force_grid_match([2, 2, 1])


class Scoprikon(Organism):
	def __init__(self):
		super().__init__("Scoprikon", "Psycho Bite+: Attacks for 15 HP and drains 3 Mana from opponent's monsters.", 6, mana_indexes['psychic'], None)

	def ability(self):
		self.game.next_player.change_HP(-15)
		for organism in self.game.next_player.organisms:
			organism.change_num_mana(-3)


class Barbenin(Organism):
	def __init__(self):
		super().__init__("Barbenin", "Psycho Bite: Attacks for 10 HP and drains 2 Mana from opponent's monsters.", 6, mana_indexes['psychic'], Scoprikon)

	def ability(self):
		self.game.next_player.change_HP(-10)
		for organism in self.game.next_player.organisms:
			organism.change_num_mana(-2)


class Magnooki(Organism):
	def __init__(self):
		super().__init__("Magnooki", 'Pyro Blitz+: Attacks for 35 HP and matches a random row.', 10, mana_indexes['fire'], None)

	def ability(self):
		self.game.next_player.change_HP(-35)
		self.game.grid.force_grid_match([1, -1, 1])


class Pyrokun(Organism):
	def __init__(self):
		super().__init__("Pyrokun", 'Pyro Blitz: Attacks for 25 HP and matches a random row.', 10, mana_indexes['fire'], Magnooki)

	def ability(self):
		self.game.next_player.change_HP(-25)
		self.game.grid.force_grid_match([1, -1, 1])


class Shardivore(Organism):
	def __init__(self):
		super().__init__("Shardivore", 'Aqua Blast+: Attacks for 25 HP and converts 3 random tiles to Water.', 10, mana_indexes['water'], None)

	def ability(self):
		self.game.next_player.change_HP(-25)
		self.game.grid.convert_tiles(self.mana_type_index, 3)


class Trashark(Organism):
	def __init__(self):
		super().__init__("Trashark", 'Aqua Blast: Attacks for 20 HP and converts 2 random tiles to Water.', 10, mana_indexes['water'], Shardivore)

	def ability(self):
		self.game.next_player.change_HP(-20)
		self.game.grid.convert_tiles(self.mana_type_index, 2)

class TurnStartEvent(ABC):
	def __init__(self, max_num_turns_active, game):
		self.curr_num_turns_active = 0
		self.max_num_turns_active = max_num_turns_active
		self.game = game
		# Caching the players, cause current and next player switch around
		self.curr_player = self.game.curr_player
		self.next_player = self.game.next_player
		self.subscribed = True

	def act(self):
		# Unsubscribing the event
		self.curr_num_turns_active += 1
		if self.curr_num_turns_active == self.max_num_turns_active:
			self.subscribed = False

class TurnEndEvent(ABC):
	def __init__(self, max_num_turns_active, game):
		self.curr_num_turns_active = 0
		self.max_num_turns_active = max_num_turns_active
		self.game = game
		# Caching the players, cause current and next player switch around
		self.curr_player = self.game.curr_player
		self.next_player = self.game.next_player
		self.subscribed = True

	def act(self):
		# Unsubscribing the event
		self.curr_num_turns_active += 1
		if self.curr_num_turns_active == self.max_num_turns_active:
			self.subscribed = False


class FlowerDance(TurnEndEvent):
	def __init__(self, max_num_turns_active, game, heal, damage):
		super().__init__(max_num_turns_active, game)
		self.heal = heal
		self.damage = damage

	def act(self):
		self.next_player.change_HP(self.damage)
		self.curr_player.change_HP(self.heal)
		super().act()


class Eidelf(Organism):
	def __init__(self):
		super().__init__("Eidelf", 'Flower Dance+: Attacks for 5 HP and heals 10 HP at the end of the turn for two turns.', 6, mana_indexes['grass'], None)

	def ability(self):
		self.game.turn_end_events.append(FlowerDance(2, self.game, 5, -10))


class Elfini(Organism):
	def __init__(self):
		super().__init__("Elfini", 'Flower Dance: Attacks for 5 HP and heals 5 HP at the end of the turn for two turns.', 6, mana_indexes['grass'], Eidelf)

	def ability(self):
		self.game.turn_end_events.append(FlowerDance(2, self.game, 5, -5))


class Starblitz(TurnEndEvent):
	def act(self):
		if self.curr_num_turns_active == 1:
			self.curr_player.moves += 1
		super().act()


class Gleamur(Organism):
	def __init__(self):
		super().__init__("Gleamur", 'Starblitz+: Attacks for 15 HP and grants 1 extra move in the next turn.', 6, mana_indexes['electric'], None)

	def ability(self):
		self.game.next_player.change_HP(-15)
		self.game.turn_start_events.append(Starblitz(1, self.game))


class Winklit(Organism):
	def __init__(self):
		super().__init__("Winklit", 'Starblitz: Attacks for 10 HP and grants 1 extra move in the next turn.', 6, mana_indexes['electric'], Gleamur)

	def ability(self):
		self.game.next_player.change_HP(-10)
		self.game.turn_start_events.append(Starblitz(1, self.game))


class Flambagant(Organism):
	def __init__(self):
		super().__init__("Flambagant", 'Hugs+: Attacks for 15 HP and gives 3 mana to your other monster.', 6, mana_indexes['fire'], None)

	def ability(self):
		self.game.next_player.change_HP(-15)
		index_of_self = self.game.curr_player.organisms.index(self)
		self.game.curr_player.organisms[(index_of_self+1) % 2].change_num_mana(3)


class Timingo(Organism):
	def __init__(self):
		super().__init__("Timingo", 'Hugs: Attacks for 10 HP and gives 2 mana to your other monster.', 6, mana_indexes['fire'], Flambagant)

	def ability(self):
		self.game.next_player.change_HP(-10)
		index_of_self = self.game.curr_player.organisms.index(self)
		self.game.curr_player.organisms[(index_of_self+1) % 2].change_num_mana(2)


class Bandicrook(Organism):
	def __init__(self):
		super().__init__("Bandicrook", 'Pickpocket+: Attacks for 10 HP and steals up to 2 berries and 2 mana.', 6, mana_indexes['psychic'], None)

	def ability(self):
		self.game.next_player.change_HP(-10)

		num_stolen_berries = min(0, self.game.next_player.num_berries - 2) + 2
		self.game.curr_player.change_num_berries(num_stolen_berries)
		self.game.next_player.change_num_berries(-num_stolen_berries)

		organism_to_steal_mana_from = max(self.game.next_player.organisms, key=lambda x: x.num_mana)
		num_mana_stolen = min(0, organism_to_steal_mana_from.num_mana - 2) + 2
		self.change_num_mana(num_mana_stolen)
		organism_to_steal_mana_from.change_num_mana(-num_mana_stolen)


class Criminook(Organism):
	def __init__(self):
		super().__init__("Criminook", 'Pickpocket: Attacks for 10 HP and steals up to 2 berries and 1 mana.', 6, mana_indexes['psychic'], Bandicrook)

	def ability(self):
		self.game.next_player.change_HP(-10)

		num_stolen_berries = min(0, self.game.next_player.num_berries - 2) + 2
		self.game.curr_player.change_num_berries(num_stolen_berries)
		self.game.next_player.change_num_berries(-num_stolen_berries)

		organism_to_steal_mana_from = max(self.game.next_player.organisms, key=lambda x: x.num_mana)
		num_mana_stolen = min(0, organism_to_steal_mana_from.num_mana - 1) + 1
		self.change_num_mana(num_mana_stolen)
		organism_to_steal_mana_from.change_num_mana(-num_mana_stolen)


class Punish(TurnEndEvent):
	def act(self):
		if self.curr_num_turns_active >= 1:
			if self.game.curr_player == self.curr_player:
				self.curr_player.moves -= 1
		super().act()


class Wreckore(Organism):
	def __init__(self):
		super().__init__("Wreckore", 'Punish+: Attacks for 45 HP but loses 1 move for the next 2 turns.', 10, mana_indexes['water'], None)

	def ability(self):
		self.game.next_player.change_HP(-45)
		self.game.turn_end_events.append(Punish(4, self.game))


class Nerverack(Organism):
	def __init__(self):
		super().__init__("Nerverack", 'Punish: Attacks for 35 HP but loses 1 move for the next 1 turn.', 10, mana_indexes['water'], Wreckore)

	def ability(self):
		self.game.next_player.change_HP(-35)
		self.game.turn_end_events.append(Punish(2, self.game))
		
class Harvest(TurnStartEvent):
	def __init__(self, max_num_turns_active, game, berries):
		super().__init__(max_num_turns_active, game)
		self.berries = berries

	def act(self):
		self.curr_player.change_num_berries(berries)
		super().act()
		
class Birchard(Organism):
	def __init__(self):
		super().__init__("Birchard", 'Harvest+: Attacks for 15 HP & adds 2 berries at the start of your next turn.', 5, mana_indexes['grass'], None)

	def ability(self):
		self.game.next_player.change_HP(-15)
		self.game.turn_start_events.append(Harvest(1, self.game, 2))
		
class Birchee(Organism):
	def __init__(self):
		super()__init__("Birchee", 'Harvest: Attacks for 10 HP & adds 1 berry on your next turn for 2 turns.', 6, mana_indexes['grass'], Birchard)

	def ability(self):
		self.game.next_player.change_HP(-10)
		self.game.turn_start_events.append(Harvest(2, self.game, 1))
	
stage_1_organisms = [Bonzumi(), Pelijet(), Turtleisk(), Slickitty(), Barbenin(), Pyrokun(), Trashark(), Elfini(), Winklit(), Timingo(), Criminook(), Nerverack(), Birchee()]
