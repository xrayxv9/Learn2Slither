from map import Map


class Apple:
    def __init__(self, color: str) -> None:
        self.color: str = color
        self.coo: tuple[int, int]

    def displace(self, map: Map):
        save_coo = self.coo
        self.coo = map.generate_new_position()
        map.update_map(save_coo, self.coo, self.color)
