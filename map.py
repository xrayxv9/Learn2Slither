from random import choice
from enums import X, Y, Update_map


class Map:
    def __init__(self) -> None:
        self._map: list[list[str]] = [
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', '0', '0', '0', '0', '0', '0', '0', '0', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ]

        self.last_action: Update_map

    def get_map(self) -> list[list[str]]:
        return (self._map)

    def __get_zero(self) -> list[tuple[int, int]]:
        ret_value: list[tuple[int, int]] = []

        for y_idx, row in enumerate(self._map):
            for x_idx, cell in enumerate(row):
                if cell == '0':
                    ret_value.append((y_idx, x_idx))

        return ret_value

    def generate_new_position(self) -> tuple[int, int]:
        positions: list[tuple[int, int]] = self.__get_zero()

        return choice(positions)

    def check_availibility(self, coo: tuple[int, int]) -> bool:
        if (self._map[coo[Y]][coo[X]] == '0'):
            return True

        return False

    def update_map(
            self,
            saved_coo: tuple[int, int],
            new_coo: tuple[int, int],
            character: str = 'H'
    ) -> Update_map:

        self.last_action = Update_map.NOTHING

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
