from ex02.mass import Mass
from ex03.length import Length


class Body:
    def __init__(self, weight, height):
        self.__weight = weight if isinstance(weight, Mass) else Mass(0) # Verifie que c'est bien un objet, une instance de la classe Mass()
        self.__height = height if isinstance(height, Length) else Length(0)

    def __str__(self):
        print(f'{self.__class__.__name__}(weight: {self.__weight:.2f} kg, size: {self.__height:.2f} m)')

    def __repr__(self):
        """ {self.__class__.__name__:.2f} recherche le nom de la classe actuelle """

        return str(self)

    def get_bmi(self):
        poids = self.__weight.in_kilos()
        taille = self.__height.squared().in_meters()

        if taille > 0:
            imc = poids / taille

            return imc
        else:
            return 0

    @property
    def weight(self):
        return Mass(self.__weight.in_kilos())

    @property
    def height(self):
        return Length(self.__height.in_meters())


