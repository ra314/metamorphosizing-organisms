import random
from Player import Player
from Grid import Grid


class Game:
    # Height and width
    grid_size = (5, 7)

    def __init__(self, player1, player2):
        self._players = (player1, player2)
        self._curr_player = None
        self._next_player = None
        self._grid = Grid(self.grid_size)
        self.display_buffer = []
        self._start()

    def request_input(self):
        return self._curr_player.name, self._curr_player.get_actions()

    def _start(self):
        self._randomise_arena()
        self._select_first_player()
        self._update_grid()

    def _randomise_arena(self):
        arenas = {'stadium': "Stadium: Each player has 60 starting HP",
                  'forest valley': "Forest Valley: 1 less Berry to evolve",
                  'abandoned town': "Abandoned Town: Evolving restores 10 HP"}
        arena = random.choice(list(arenas.keys()))

        if arena == 'stadium':
            Player.max_HP = 60
            # noinspection PyPep8Naming
            self._players[0].curr_HP = 60
            # noinspection PyPep8Naming
            self._players[1].curr_HP = 60

        elif arena == 'forest valley':
            Player.berries_to_evolve -= 1

        elif arena == 'abandoned town':
            Player.HP_restored_on_evolution = 10

        self.display_buffer.append(arenas[arena])

    def _update_grid(self):
        while self._grid.display_buffer:
            self.display_buffer.append(f'{self._players[0].display()} \n\n'
                                       f'{self._players[1].display()} \n\n'
                                       f'{self._grid.display_buffer.pop(0)}')

    def _select_first_player(self):
        players = list(self._players)
        random.shuffle(players)
        self._curr_player, self._next_player = players
        self._next_player.curr_HP += 5
        self.display_buffer.append(f'The first player is {self._curr_player.name}. \n'
                                   f'{self._next_player.name} gets + 5 HP.')
