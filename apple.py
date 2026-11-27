class Apple:
    def __init__(self, color: str) -> None:
        self.color: str = color
        self.coo: tuple[int, int] | None

    def displace(self, new_coords: tuple[int, int] | None):
        self.coo = new_coords

    def get_coo(self) -> tuple[int, int] | None:
        return self.coo

    def get_type(self) -> str:
        return self.color
