# operator.py
from Member import Member


class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = 0

    # Getters
    def get_role(self):
        return self.__role

    def get_experience(self):
        return self.__experience

    # Setters
    def set_role(self, new_role):
        self.__role = new_role

    def set_experience(self, new_exp):
        self.__experience = max(0, int(new_exp))

    # Définition d'une méthode qui dit ce que fait l'Operator selon son role

    def act(self):
        full_name = f"{self.get_first_name()} {self.get_last_name()}"
        r = self.get_role().lower()

        match r:
            case "pilote":
                print(f"{full_name} pilote le vaisseau")
            case "technicien":
                print(f"{full_name} répare le vaisseau")
            case _:
                print(f"{full_name} ne fait rien")

    # ---------- Méthodes métier ----------
    def gain_experience(self, amount=1):
        """
        Incrémente l'expérience (par défaut +1).
        """
        self.__experience = self.__experience + int(amount)
