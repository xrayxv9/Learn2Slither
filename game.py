from agent import Agent
from enums import X, Y, Update_map
from map import Map
from watcher import Watcher
import subprocess

class Game:
    def __init__(self, map_size: int) -> None:
        self.map_size: int = map_size

        self.map: Map = Map(map_size)
        self.head: Agent
        self.watcher: Watcher

    def restart(self) -> None:
        # map init
        self.map = Map(self.map_size)
        spawn = self.map.snake_spawn()

        # Head init
        self.head = Agent(spawn[Y], spawn[X])
        self.head.spawn()

        # watcher init
        self.watcher = Watcher(self.head, self.map)
        self.watcher.update_env()

    def game_loop(self) -> None:
        self.restart()
        run = True

        while run:
            subprocess.run(['clear'])
            self.map.print_map()
            inp = input("what to do ? (a, s, d, w)")
            if (inp == 'quit'):
                run = False
            elif (inp == 'a'):
                self.head.go_left()
            elif (inp == 's'):
                self.head.go_down()
            elif (inp == 'd'):
                self.head.go_right()
            else:
                self.head.go_up()
            exit_status = self.watcher.update_env()
            if Update_map.WON == exit_status:
                print("You Won !")
                subprocess.run(['sleep', '2'])
                self.restart()
            elif (exit_status == Update_map.TAIL or exit_status == Update_map.WALL):
                print(f"You lost due to: {'your tail' if exit_status == Update_map.TAIL else 'a wall'}")
                subprocess.run(['sleep', '2'])
                self.restart()

