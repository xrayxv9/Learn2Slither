from agent import Agent
from apple import Apple
from enums import Y, X, Update_map
from map import Map

class Watcher:
    def __init__(self, head: Agent, map: Map) -> None:
        self.head: Agent = head
        self.mapObj: Map = map
        self.apples: list[Apple] = [Apple('G'), Apple('G'), Apple('R')]
        for apple in self.apples:
            apple.displace(self.mapObj.generate_new_position(apple.get_type()))

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

        for y in range(len(self.mapObj.get_map())):
            if y == head_position[Y]:
                pass
            elif y < head_position[Y]:
                vision["up"].append(map[y][head_position[X]])
            else:
                vision["bot"].append(map[y][head_position[X]])

        for x in range(len(self.mapObj.get_map())):
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

    def print_vision(self):
        self.head.print_vision()


    def init_apples(self):
        for apple in self.apples:
            apple.displace(self.mapObj.generate_new_position(apple.get_type()))

    def update_env(self) -> Update_map:
        self.mapObj.update_map(self.head, self.apples)
        match self.mapObj.get_state():
            case Update_map.GREEN_APPLE_EATEN:
                self.head.grow()
            case Update_map.RED_APPLE_EATEN:
                self.head.shrink()
            case Update_map.TAIL | Update_map.WALL:
                return self.mapObj.get_state()
        self.mapObj.update_map(self.head, self.apples)
        if (self.mapObj.finished()):
            return Update_map.WON

        return Update_map.NOTHING
