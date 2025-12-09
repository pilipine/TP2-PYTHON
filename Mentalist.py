# Import de la classe Member depuis son module
from Member import Member
from Operator import Operateur

# Constantes liées à la classe Mentalist
MIN_MANA = 0
MAX_MANA = 100
TELEKINESIS_MANA_COST = 60
RECHARGE_MANA_VALUE = 50


class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age, mana=MAX_MANA):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = int(mana)
        self.set_role("Mentalist")

    # --------- Getter/Setter mana ----------
    def get_mana(self) -> int:
        return self.__mana

    def set_mana(self, new_mana):
        self.__mana = max(0, int(new_mana))  # on évite les valeurs négatives

    def augmentation_mana(self, add_mana):
        self.__mana += add_mana
        if self.__mana > MAX_MANA:
            self._mana = MAX_MANA

    def baisse_mana(self, sub_mana):
        self.__mana -= sub_mana
        if self.get_mana() < MIN_MANA:
            self.__mana = MIN_MANA


# Définition d'une méthode qui lance un sort télékinésique sur un Operator, lui faisaint dire ce qu'il fait
