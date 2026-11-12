

from typing import Callable


class tail:
    def __init__(self, next_tail: tail | None = None) -> None:
        self.next: tail | None = next_tail;
        next_action: Callable[[], None];
        last_action: Callable[[], None];


