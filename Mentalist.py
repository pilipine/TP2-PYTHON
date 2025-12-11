# Import de la classe Member depuis son module
from Member import Member
from Operator import Operator

# Constantes liées à la classe Mentalist
MIN_MANA = 0
MAX_MANA = 100
NOMBRE_MANA_PERDU = 20
RECHARGE_MANA = 50


class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age, mana=MAX_MANA):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = int(mana)
        #self.set_role("Mentalist")

    # --------- Getter/Setter mana ----------
    def get_mana(self):
        return self.__mana

    def set_mana(self, new_mana):
        self.__mana = max(0, int(new_mana)) 


    def augmentation_mana(self, add_mana):
        self.__mana += (add_mana)
        if self.__mana > MAX_MANA:        
            self.__mana = MAX_MANA

    def baisse_mana(self, sub_mana):
        self.__mana -= (sub_mana)
        if self.__mana < MIN_MANA:
            self.__mana = MIN_MANA


# Définition act() : réduit les points de mana de 20; influence un opérateur en le forçant a agir
    def act (self,target):
        self.baisse_mana(NOMBRE_MANA_PERDU)
        if target.get_role() != None and target.get_role().lower() == "mentalist":
            print("Je ne peux pas lancer un sort sur un mentaliste")
        elif target.get_role() != None and target.get_role().lower() != "mentalist":target.act()

 # Définition recharge_mana(): augmente les points de 50sans dépasser les 100
    def recharge_mana(self):
        self.augmentation_mana(RECHARGE_MANA)
