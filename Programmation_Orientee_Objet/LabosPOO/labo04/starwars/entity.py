class Entity:
    def __init__(self, name, hit_points):
        self.__name = name
        self.__hit_points = hit_points

    @property
    def name(self):
        return self.__name

    @property
    def hit_points(self):
        return self.__hit_points

    def take_hit(self, damage):
        self.__hit_points = self.__hit_points - damage
        return self.__hit_points

    def is_alive(self):
        if self.hit_points > 0:
            return True
        else:
            return False