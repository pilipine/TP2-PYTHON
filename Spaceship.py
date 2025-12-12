# spaceship.py
# Imports des classes


class Spaceship:
    def __init__(self, name, ship_type, crew=[], condition="Opérationnel"):
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = crew
        self.__condition = condition

    # --------- Getter/Setter mana ----------
    def get_name(self):
        return self.__name

    def get_ship_type(self):
        return self.__ship_type

    def get_crew(self):
        return self.__crew

    def get_condition(self):
        return self.__condition

    def set_name(self, new_name):
        self.__name = new_name

    def set_ship_type(self, new_ship_type):
        self.__ship_type = new_ship_type

    def set_crew(self, new_crew):
        self.__crew = new_crew

    def set_condition(self, new_condition):
        self.__condition = new_condition

    # Méthodes classe Spaceship

    def append_member(self, member):
        if len(self.__crew) >= 10:
            print(
                "la capacité maximale de 10 membres d'équipage par vaisseau est atteinte"
            )
            # return False
        elif self.__crew.append(member):
            print("Bienvenue à bord")
            # return True

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

            # Si les deux sont trouvés
            if has_pilot and has_technician:
                return True

        # Après la boucle, on retourne True seulement si les deux sont présents
        if has_pilot and has_technician:
            return True
        else:
            return False
