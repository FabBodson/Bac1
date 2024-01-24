
class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @property
    def volume(self):
        return self.length * self.width * self.height

    @property
    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)


class Cube(Cuboid):
    def __init__(self, length):
        super().__init__(length, length, length)
