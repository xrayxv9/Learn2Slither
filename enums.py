from enum import Enum

X = 1


Y = 0


class Update_map(Enum):
    GREEN_APPLE_EATEN = 1
    RED_APPLE_EATEN = -1
    NOTHING = 0
    WALL = -2
    TAIL = -3
