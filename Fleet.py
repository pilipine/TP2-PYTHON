from Operator import *
from Mentalist import *
from Spaceship import *


class Fleet:
    def __init__(self, name, Spaceship):
        self.__name = name
        self.__Spaceship = []

    # --------- Getter/Setter mana ----------
    def get_name(self):
        return self.__name

    def get_Spaceship(self):
        return self.__Spaceship

    def set_name(self, new_name):
        self.__name = new_name

    def set_Spaceship(self, new_Spaceship):
        self.__ship_type = new_Spaceship

    # Définition d'une méthode qui ajoute un vaisseau à la flotte
    def append_spaceships(self, Spaceships):
        if len(self.__Spaceships) > 15:
            print("Ce vaisseaux ne peut pas être ajouter de flotte")

    # Définition d'une méthode renvoyant un dictionnaire avec les statistiques de l'équipage de chaque vaisseau de la flotte
    def statistics(self):
        total_experience = 0
        total_members = 0
        role_member = {"mentalist": 0, "operator": 0}
        for spaceship in self.__Spaceships:
            for member in spaceship.get_crew():
                if type(member) is Operator:
                    total_experience += member.get_experience()
                    role = member.get_role().lower()
                    if role not in role_member:
                        role_member[role] = 1
                    else:
                        role_member[role] += 1
                total_members += 1
                if type(member) is Mentalist:
                    role_member["mentalist"] += 1

        average_experience = (
            total_experience / total_members if total_members > 0 else 0
        )

        return {
            "nombre_de_vaisseaux": len(self.__Spaceships),
            "moyenne_experience": average_experience,
            "repartition_roles": role_member,
        }
