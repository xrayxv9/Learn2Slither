from random import choice, randint
from apple import Apple
from agent import Agent
from enums import X, Y, Update_map


class Map:
    def __init__(self, map_size: int) -> None:
        self._map: list[list[str]] = [
            ['W'] * map_size if i == 0 or i == map_size - 1 else ['W'] + ['0'] * (map_size - 2) + ['W']
            for i in range(map_size)
        ]
        self.map_size = map_size
        self.last_action: Update_map

    def get_map(self) -> list[list[str]]:
        return (self._map)

    def print_map(self) -> None:
        for line in self._map:
            for row in line:
                print(f'{row}', end='')
            print('')

    def __get_zero(self) -> list[tuple[int, int]]:
        ret_value: list[tuple[int, int]] = []

        for y_idx, row in enumerate(self._map):
            for x_idx, cell in enumerate(row):
                if cell == '0':
                    ret_value.append((y_idx, x_idx))

        return ret_value

    def snake_spawn(self) -> list[tuple[int, int]]:
        line = randint(1, self.map_size - 2)
        row= randint(3, self.map_size - 2)
        ret = [(line, row), (line, row - 1), (line, row - 2)]

        self._map[ret[0][0]][ret[0][1]] = 'H'
        self._map[ret[1][0]][ret[1][1]] = 'S'
        self._map[ret[2][0]][ret[2][1]] = 'S'
        return ret

    def generate_new_position(self) -> tuple[int, int]:
        positions: list[tuple[int, int]] = self.__get_zero()
        return choice(positions)

    def check_availibility(self, coo: tuple[int, int]) -> bool:
        if (self._map[coo[Y]][coo[X]] == '0'):
            return True

        return False

    def update_map(
        self,
        head: Agent,
        apples: list[Apple]
    ) -> Update_map:

        self.last_action = Update_map.NOTHING

        head_coo: tuple[int, int] = head.get_coo()
        # TODO
        # change the all update_map system to update depending on the coordonates
        # the changes events should be detected with the watcher BE CAREFUL

        if self._map[saved_coo[Y]][saved_coo[X]] == 'G' and character != 'G':
            self._map[saved_coo[Y]][saved_coo[X]] = '0'
            self._map[new_coo[Y]][new_coo[X]] = character
            self.last_action = Update_map.GREEN_APPLE_EATEN

        elif self._map[saved_coo[Y]][saved_coo[X]] == 'R' and character != 'R':
            self._map[saved_coo[Y]][saved_coo[X]] = character
            self.last_action = Update_map.RED_APPLE_EATEN

        elif self._map[new_coo[Y]][new_coo[X]] == 'W':
            self.last_action = Update_map.WALL

        elif self._map[new_coo[Y]][new_coo[X]] == 'S':
            self.last_action = Update_map.TAIL

        else:
            self._map[saved_coo[Y]][saved_coo[X]] = '0'
            self._map[new_coo[Y]][new_coo[X]] = character

        return self.last_action
