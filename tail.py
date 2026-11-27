from __future__ import annotations
from collections import deque
from typing import Callable
from enums import X, Y


class Tail:
    def __init__(
        self,
        coo_y: int,
        coo_x: int,
        actions_to_do: deque[str],
        next_tail: Tail | None = None
    ) -> None:
        self.alive: bool = True
        self.saved_coo: tuple[int, int] = (coo_y, coo_x)
        self.next: Tail | None = next_tail
        self.actions: deque[str] = deque(actions_to_do)
        self.coo: tuple[int, int] = (coo_y, coo_x)
        self.executable: dict[str, Callable[[], None]] ={
            'up': self.go_up,
            'down': self.go_down,
            'right': self.go_right,
            'left': self.go_left
        }
        self.last_action: str;
    def act(self, new_action: str): 
        print(f"TAIL INIT | coo={self.coo} | actions={list(self.actions)}")
        match new_action:
            case 'up':
                self.actions.append('up')
            case 'down':
                self.actions.append('down')
            case 'left':
                self.actions.append('left')
            case 'right':
                self.actions.append('right')

        self.executable[self.actions.popleft()]() 
        if (self.next):
            match new_action:
                case 'up':
                    self.next.act('up')
                case 'down':
                    self.next.act('down')
                case 'left':
                    self.next.act('left')
                case 'right':
                    self.next.act('right')

    def grow(self) -> None:
        print(f"GROW: coo: {self.coo}, saved: {self.saved_coo}")
        if self.next is None:
            copy = deque(self.actions)
            copy.appendleft(self.last_action)
            self.next = Tail(
                self.saved_coo[Y],
                self.saved_coo[X],
                copy,
            )
            print(f"GROW: coo: {self.next.coo}, saved: {self.next.saved_coo}")
        else:
            self.next.grow()

    def shrink(self) -> None:
        if (self.next is not None and
            self.next.next is None):
            self.next.alive = False
        elif (self.next is not None and
              self.next.next is not None):
            self.next.shrink()

    def set_up_actions(self, action: deque[str]):
        self.actions = action

    def get_coo(self) -> tuple[int, int]:
        return self.coo
        
    def get_saved_coo(self) -> tuple[int, int]:
        return self.saved_coo

    def go_up(self) -> None:
        self.saved_coo = self.coo
        self.coo = (self.coo[Y] - 1, self.coo[X])
        self.last_action = 'up'

    def go_down(self) -> None:
        self.saved_coo = self.coo
        self.coo = (self.coo[Y] + 1, self.coo[X])
        self.last_action = 'down'

    def go_right(self) -> None:
        self.saved_coo = self.coo
        self.coo = (self.coo[Y], self.coo[X] + 1)
        self.last_action = 'right'

    def go_left(self) -> None:
        self.saved_coo = self.coo
        self.coo = (self.coo[Y], self.coo[X] - 1)
        self.last_action = 'left'
