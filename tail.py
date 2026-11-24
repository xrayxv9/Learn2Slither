from __future__ import annotations
from collections import deque
from typing import Callable
from enums import X, Y, Update_map
from map import Map


class Tail:
    def __init__(
        self,
        coo_y: int,
        coo_x: int,
        actions_to_do: deque[Callable[[], None]],
        next_tail: Tail | None = None
    ) -> None:

        self.next: Tail | None = next_tail
        self.actions: deque[Callable[[], None]] = deque(actions_to_do)
        self.coo: tuple[int, int] = (coo_y, coo_x)

    def act(self, eaten: Update_map, new_action: Callable[[], None]):
        self.actions.append(new_action)

        if eaten:
            if (eaten == Update_map.GREEN_APPLE_EATEN and self.next is None):
                self.next = Tail(
                    self.coo[Y],
                    self.coo[X],
                    self.actions,
                )
            if (
                eaten == Update_map.RED_APPLE_EATEN and
                self.next is not None and
                self.next.next is None
            ):
                self.next = None

        self.actions.popleft()()
        if (self.next):
            self.next.act(eaten, new_action)

    def set_up_actions(self, action: deque[Callable[[], None]]):
        self.actions = action
        
    def go_up(self) -> None:
        self.coo = (self.coo[Y] + 1, self.coo[X])

    def go_down(self) -> None:
        self.coo = (self.coo[Y] - 1, self.coo[X])

    def go_right(self) -> None:
        self.coo = (self.coo[Y], self.coo[X] + 1)

    def go_left(self) -> None:
        self.coo = (self.coo[Y], self.coo[X] - 1)
