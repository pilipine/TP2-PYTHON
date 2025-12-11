
# spaceship.py
# Imports des classes 
from Member import Member
from Operator import Operator
from Mentalist import Mentalist


class Spaceship:

    def __init__(self, first_name, last_name, gender, age, name, shiptype, crew, condition):
        super().__init__(first_name, last_name, gender, age)
        self.__name= name
        self.__shiptype= shiptype
        self.__crew= []
        self.__condition= condition


# --------- Getter/Setter mana ----------
    def get_mana(self) -> int:
        return self.__name
    
    def get_shiptype(self) -> int:
        return self.__shiptype
    
    def get_crew(self) -> int:
        return self.__crew
    
    def get_condition(self):
        return self.__condition
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_shiptype(self, new_shiptype):
        self.__shiptype = new_shiptype
    
    def set_crew(self, new_crew):
        self.__crew = new_crew

    def set_condition(self, new_condition):
        self.__condition = new_condition

# Méthodes classe Spaceship

    def append_member(self, member):
        if len(self.crew)>=10:
            print("la capacité maximale de 10 membres d'équipage par vaisseau est atteint")
            return False
        elif self.crew.append(member):
            return True
    
    def check_preparation(self):
        has_pilot = False
        has_technician = False

        for member in self.crew:
            if hasattr(member, "get_role"):  # Vérifie que le membre a un rôle
                role = member.get_role().lower()
                if role == "pilote":
                    has_pilot = True
                elif role == "technicien":
                    has_technician = True

        # Si les deux sont trouvés, on peut arrêter la boucle
            if has_pilot and has_technician:
                return True

    # Après la boucle, on retourne True seulement si les deux sont présents
        if has_pilot and has_technician:
            return True
        else:
            return False
