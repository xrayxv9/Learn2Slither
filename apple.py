from map import Map


class Apple:
    def __init__(self, color: str) -> None:
        self.color: str = color
        self.coo: tuple[int, int]

    def displace(self, map: Map):
        save_coo = self.coo
        self.coo = map.generate_new_position()

    def get_coo(self) -> tuple[int, int]:
        return self.coo

    def get_type(self) -> str:
        return self.color
