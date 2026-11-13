from map import Map
from agent import Agent


class Game:

    def __init__(self, map_y: int, map_x: int) -> None:
        self.map = Map()
        self.agent = Agent()
