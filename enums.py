from enum import Enum

X = 1
Y = 0
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ORANGE = '\033[38;5;208m'
YELLOW = '\033[38;5;226m'


class Update_map(Enum):
    WON = 5
    GREEN_APPLE_EATEN = 1
    RED_APPLE_EATEN = -1
    NOTHING = 0
    WALL = -2
    TAIL = -3
