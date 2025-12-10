# Import de la classe Member
from Member import *  # ou: from classes.member import Member


class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = int(experience)

    # Getters
    def get_role(self):
        return self.__role

    def get_experience(self):
        return self.__experience

    # Setters
    def set_role(self, new_role):
        self.__role = new_role

    def set_experience(self, new_experience):
        self.__experience = int(new_experience)

    # Définition d'une méthode qui dit ce que fait l'Operator selon son role
    def act(self):
        if self.get_role() == "pilot":
            print(f"{self.get_first_name()} {self.get_last_name()} pilote le vaisseau")
        if self.get_role().lower() == "technician":
            print(f"{self.get_first_name()} {self.get_last_name()} répare le vaisseau")
        else:
            print("Ne fait rien")

    def gain_experience(self):
        self.__experience = self.__experience + 1
