from __future__ import annotations
from typing import Callable


class Tail:
    def __init__(
        self,
        coo_x: int,
        coo_y: int,
        next_tail: Tail | None = None
    ) -> None:

        self.next: Tail | None = next_tail
        self.next_action: Callable[[], None]
        self.last_action: Callable[[], None]
        self.coo: tuple[int, int] = (coo_x, coo_y)

    def go_up(self) -> None:
        self.coo = (self.coo[0], self.coo[1] + 1)

    def go_down(self) -> None:
        self.coo = (self.coo[0], self.coo[1] - 1)

    def go_right(self) -> None:
        self.coo = (self.coo[0] + 1, self.coo[1])

    def go_left(self) -> None:
        self.coo = (self.coo[0] - 1, self.coo[1])

    def set_next_action(self, action: Callable[[], None]):
        self.next_action = action

    def grow(self):
        if self.next is None:
            self.next = Tail(self.coo[0], self.coo[1])
            self.next.set_next_action(self.last_action)
        else:
            self.next.grow()
