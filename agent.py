

class agent:
    def __init__(self, coo_x: int, coo_y: int) -> None:
        self._vision: dict[str, list[str]] = {
            'right': [],
            'left': [],
            'bot': [],
            'up': [],
        }

        self.coo: tuple[int, int] = (coo_x, coo_y)

    def update_vision(self, vision: dict[str, list[str]]) -> None:
        self.vision = vision

    def go_up(self) -> None:
        self.coo = (self.coo[0], self.coo[1] + 1)

    def go_down(self) -> None:
        self.coo = (self.coo[0], self.coo[1] - 1)

    def go_right(self) -> None:
        self.coo = (self.coo[0] + 1, self.coo[1])

    def go_left(self) -> None:
        self.coo = (self.coo[0] - 1, self.coo[1])
