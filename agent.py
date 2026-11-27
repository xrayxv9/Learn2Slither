from collections import deque
from enums import Y, X
import tail


class Agent:
    def __init__(self, coo_y: int, coo_x: int) -> None:
        self._vision: dict[str, list[str]] = {
            'right': [],
            'left': [],
            'bot': [],
            'up': [],
        }
        self.coo: tuple[int, int] = (coo_y, coo_x)
        self.tail: tail.Tail
        self.last_action: str = 'right'

    def update_vision(self, vision: dict[str, list[str]]) -> None:
        self._vision = vision

    def spawn(self) -> None:
        self.tail = tail.Tail(self.coo[Y], self.coo[X] - 1, deque())
        self.tail.set_up_actions(deque(['right']))
        self.tail.next = tail.Tail(self.coo[Y], self.coo[X] - 2, deque())
        self.tail.next.set_up_actions(deque(['right', 'right']))

    def print_vision(self):
        for up in self._vision["up"]:
            for _ in self._vision["left"]:
                print(" ", end="")
            print(up)
        for left in self._vision["left"]:
            print(left, end="")
        print("H", end="")
        for right in self._vision["right"]:
            print(right, end="")
        print()
        for bot in self._vision["bot"]:
            for _ in self._vision["left"]:
                print(" ", end="")
            print(bot)

    def grow(self):
        self.tail.grow()

    def shrink(self):
        self.tail.shrink()

    def get_coo(self) -> tuple[int, int]:
        return self.coo

    def go_up(self) -> None:
        if (self.last_action == 'down'):
            return
        self.coo = (self.coo[Y] - 1, self.coo[X])
        self.tail.act('up')
        self.last_action = 'up'

    def go_down(self) -> None:
        if (self.last_action == 'up'):
            return
        self.coo = (self.coo[Y] + 1, self.coo[X])
        self.tail.act('down')
        self.last_action = 'down'

    def go_right(self) -> None:
        if (self.last_action == 'left'):
            return
        self.coo = (self.coo[Y], self.coo[X] + 1)
        self.tail.act('right')
        self.last_action = 'right'

    def go_left(self) -> None:
        if (self.last_action == 'right'):
            return
        self.coo = (self.coo[Y], self.coo[X] - 1)
        self.tail.act('left')
        self.last_action = 'left'
