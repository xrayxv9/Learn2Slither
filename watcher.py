from re import X

from agent import Agent
from enums import Y
from map import Map

class Watcher:
    def __init__(self, head: Agent, map: Map) -> None:
        self.head: Agent = head
        self.mapObj: Map = map

    def give_env(self):
        map: list[list[str]] = self.mapObj.get_map()
        head_position: tuple[int, int] = self.find_head(map)

        if head_position[Y] == -1:
            return False
        
        vision: dict[str, list[str]] = {
            'right': [],
            'left': [],
            'bot': [],
            'up': [],
        }

        for y in range(1, 9):
            if y == head_position[Y]:
                pass
            elif y < head_position[Y]:
                vision["up"].append(map[y][head_position[X]])
            else:
                vision["bot"].append(map[y][head_position[X]])

        for x in range(1, 9):
            if x == head_position[X]:
                pass
            elif x < head_position[X]:
                vision["left"].append(map[head_position[Y]][x])
            else:
                vision["right"].append(map[head_position[Y]][x])

        self.head.update_vision(vision);

    def find_head(self, map: list[list[str]]) -> tuple[int, int]:
        for y, row in enumerate(map):
            for x, cell in enumerate(row):
                if (cell == 'H'):
                    return (y ,x)

        return (-1, -1)

        
