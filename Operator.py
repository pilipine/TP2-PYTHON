# Import de la classe Member
from Member import * 

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
        full_name = f"{self.get_first_name()} {self.get_last_name()}"
        r = (self.role or "")

        if r in ("pilot", "pilote"):
            print(f"{full_name} pilote le vaisseau")
        elif r in ("technician", "technicien", "technicienne"):
            print(f"{full_name} répare le vaisseau")
        else:
            print(f"{full_name} ne fait rien")

#class role(Operator):
    #def __init__(self, role, gain_experience):
        super().__init__(role, gain_experience)
        self.__role= role

    #def act(self):
        if self.get_role() == "pilot":
            print(f"{self.get_first_name()} {self.get_last_name()} pilote le vaisseau")
        if self.get_role().lower() == "technician":
            print(f"{self.get_first_name()} {self.get_last_name()} répare le vaisseau")
        else:
            print("Ne fait rien")

    #def gain_experience(self):
        self.__experience = self.__experience + 1
