from starwars.entity import Entity


class ForceUser(Entity):
    def __init__(self, name, hit_points, damage_points):
        super().__init__(name, hit_points)
        self.__damage_points = damage_points


    @property
    def damage_points(self):
        return self.__damage_points

    def use_force_on(self, target):
        target.take_hit(self.__damage_points)
        target.is_alive()

        return f"{self.name} projette la force sur {target.name}. Dégâts causés : {self.damage_points}"


class Jedi(ForceUser):
    def __init__(self, name, hit_points, damage_points):
        super().__init__(name, hit_points, damage_points)
        self.rage = True

    def use_force_on(self, target):

            if self.hit_points <= 2:

                if self.rage == True:
                    target.take_hit(self.damage_points*10)
                    self.rage = False
                    target.is_alive()

                    return f"{self.name} utilise la rage de la force sur {target.name}. Dégâts causés : {self.damage_points * 10}"
                else:
                    return super().use_force_on(target)

            else:
                return super().use_force_on(target)


class Sith(ForceUser):
    def __init__(self, name, hit_points, damage_points):
        super().__init__(name, hit_points, damage_points)
        self.nb_appel = 1

    def use_force_on(self, target):
        self.nb_appel = 1
        if (self.nb_appel % 3) == 0 and (self.nb_appel % 5) == 0:

            if (self.damage_points * 2) > (self.damage_points * 5):
                target.take_hit(self.damage_points * 2)
                self.nb_appel += 1
                target.is_alive()
                return f"{self.name} étrangle {target.name}. Dégâts causés : {self.damage_points * 2}"

            else:
                target.take_hit(self.damage_points * 5)
                self.nb_appel += 1
                target.is_alive()
                return f"{self.name} lance des éclairs sur {target.name}. Dégâts causés : {self.damage_points * 5}"

        elif (self.nb_appel % 3) == 0:
            target.take_hit(self.damage_points * 2)
            self.nb_appel += 1
            target.is_alive()

            return f"{self.name} étrangle {target.name}. Dégâts causés : {self.damage_points * 2}"


        elif (self.nb_appel % 5) == 0:
            target.take_hit(self.damage_points * 5)
            self.nb_appel += 1
            target.is_alive()

            return f"{self.name} lance des éclairs sur {target.name}. Dégâts causés : {self.damage_points * 5}"


        else:
            self.nb_appel += 1
            return super().use_force_on(target)


