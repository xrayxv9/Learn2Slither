from random import choice, randint
from apple import Apple
from agent import Agent
from enums import ENDC, OKBLUE, OKCYAN, OKGREEN, ORANGE, RED, WARNING, X, Y, YELLOW, Update_map


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
                if (row == 'G'):
                    print(f'{OKGREEN}{row}{ENDC}', end='')
                elif (row == 'R'):
                    print(f'{WARNING}{row}{ENDC}', end='')
                elif (row == 'H'):
                    print(f'{ORANGE}{row}{ENDC}', end='')
                elif (row == 'S'):
                    print(f'{OKCYAN}{row}{ENDC}', end='')
                elif (row == 'W'):
                    print(f'{YELLOW}{row}{ENDC}', end='')
                else:
                    print(f'{row}', end='')
            print('')

    def __get_zero(self) -> list[tuple[int, int]]:
        ret_value: list[tuple[int, int]] = []

        for y_idx, row in enumerate(self._map):
            for x_idx, cell in enumerate(row):
                if cell == '0':
                    ret_value.append((y_idx, x_idx))

        return ret_value

    def finished(self) -> bool:
        for row in self._map:
            for cell in row:
                if cell == '0' or cell == 'G':
                    return False
        return True



    def snake_spawn(self) -> list[tuple[int, int]]:
        line = randint(1, self.map_size - 2)
        row= randint(3, self.map_size - 2)
        ret = [(line, row), (line, row - 1), (line, row - 2)]

        self._map[ret[0][0]][ret[0][1]] = 'H'
        self._map[ret[1][0]][ret[1][1]] = 'S'
        self._map[ret[2][0]][ret[2][1]] = 'S'
        return ret

    def generate_new_position(self, color: str) -> tuple[int, int] | None:
        positions: list[tuple[int, int]] = self.__get_zero()
        ret = choice(positions) if positions else None
        if ret is not None:
            self._map[ret[Y]][ret[X]] = color
        return ret
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
        current_coo = head.get_coo()
        current_square = self._map[current_coo[0]][current_coo[1]]

        match current_square:
            case 'G':
                self.last_action = Update_map.GREEN_APPLE_EATEN
                for apple in apples:
                    if (apple.get_coo() == current_coo):
                        new_coords = self.generate_new_position(apple.get_type())
                        apple.displace(new_coords);
                        if (new_coords is not None):
                            self._map[new_coords[Y]][new_coords[X]] = 'G'
            case 'R':
                self.last_action = Update_map.RED_APPLE_EATEN
                for apple in apples:
                    if (apple.get_coo() == current_coo):
                        new_coords = self.generate_new_position(apple.get_type())
                        apple.displace(new_coords);
                        if (new_coords is not None):
                            self._map[new_coords[Y]][new_coords[X]] = 'R'
            case 'W':
                self.last_action = Update_map.WALL
            case 'S':
                tail = head.tail
                while tail is not None:
                    if (current_coo == tail.get_coo()):
                        self.last_action = Update_map.TAIL
                    tail = tail.next

        snake_coo = current_coo
        
        tail = head.tail
        while (tail!= None):
            current_coo = tail.get_coo()
            saved_coo = tail.get_saved_coo()
            if (tail.next is not None and
                tail.next.alive == False):
                self._map[tail.next.get_coo()[0]][tail.next.get_coo()[1]] = '0'
                tail.next = None
            self._map[current_coo[0]][current_coo[1]] = 'S'
            if (saved_coo != current_coo):
                self._map[saved_coo[0]][saved_coo[1]] = '0'
            tail = tail.next

        i: int = 0
        for apple in apples:
            coo = apple.get_coo()
            if (coo is not None):
                self._map[coo[Y]][coo[X]] = apple.get_type()
            i+=1

        self._map[snake_coo[0]][snake_coo[1]] = 'H'
        return self.last_action

    def get_state(self) -> Update_map:
        return self.last_action
