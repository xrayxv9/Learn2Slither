from collections import deque

import tail

class Agent:
    def __init__(self, coo_x: int, coo_y: int) -> None:
        self._vision: dict[str, list[str]] = {
            'right': [],
            'left': [],
            'bot': [],
            'up': [],
        }

        self.coo: tuple[int, int] = (coo_x, coo_y)
        self.tail: tail.Tail
    def update_vision(self, vision: dict[str, list[str]]) -> None:
        self.vision = vision

    def spawn(self) -> None:
        self.tail = tail.Tail(self.coo[0], self.coo[1] - 1, deque())
        self.tail.set_up_actions(deque([self.tail.go_right]))
        self.tail.next = tail.Tail(self.coo[0], self.coo[1] - 2, deque())
        self.tail.next.set_up_actions(deque([self.tail.go_right, self.tail.go_right]))

    def get_coo(self) -> tuple[int, int]:
        return self.coo

    def go_up(self) -> None:
        self.coo = (self.coo[0], self.coo[1] + 1)

    def go_down(self) -> None:
        self.coo = (self.coo[0], self.coo[1] - 1)

    def go_right(self) -> None:
        self.coo = (self.coo[0] + 1, self.coo[1])

    def go_left(self) -> None:
        self.coo = (self.coo[0] - 1, self.coo[1])
