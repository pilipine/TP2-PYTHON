# Fleet.py
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship


class Fleet:
    def __init__(self, name, spaceships=None):
        """
        name: str
        spaceships: iterable de Spaceship ou None
        """
        self.__name = name
        self.__spaceships = list(spaceships) if spaceships is not None else []

    # --------- Getters / Setters ----------
    def get_name(self):
        return self.__name

    def set_name(self, new_name: str):
        self.__name = new_name

    def get_spaceships(self):
        # Retourne une copie pour éviter la modification accidentelle
        return list(self.__spaceships)

    def set_spaceships(self, new_spaceships):
        if not all(isinstance(s, Spaceship) for s in new_spaceships):
            raise TypeError("Tous les éléments doivent être des Spaceship.")
        self.__spaceships = list(new_spaceships)

    # --------- Ajout d'un vaisseau ----------
    def append_ship(self, ship):
        """Ajoute un vaisseau (capacité max 15). Retourne True/False."""
        if not isinstance(ship, Spaceship):
            print("[ERR] Doit être une instance de Spaceship.")
            return False
        if len(self.__spaceships) >= 15:
            print("[WARN] Capacité max de 15 vaisseaux atteinte.")
            return False
        self.__spaceships.append(ship)
        print(f"[OK] '{ship.get_name()}' ajouté à la flotte '{self.get_name()}'.")
        return True

    # Alias optionnel pour compat avec d'autres appels
    def add_ship(self, ship):
        return self.append_ship(ship)

    # --------- Statistiques ----------
    def statistics(self):
        """
        Retourne un dict avec :
        - nombre_de_vaisseaux
        - moyenne_experience_operator (moyenne d'expérience des Operators uniquement)
        - repartition_roles (comptage par rôle + totaux operator/mentalist)
        - total_membres
        """
        total_experience = 0
        operator_count = 0
        total_members = 0
        role_member = {"mentalist": 0, "operator": 0}

        for spaceship in self.__spaceships:
            for member in spaceship.get_crew():
                total_members += 1
                if isinstance(member, Operator):
                    operator_count += 1
                    total_experience += member.get_experience()
                    role = (member.get_role() or "").strip().lower()
                    if role not in role_member:
                        role_member[role] = 1
                    else:
                        role_member[role] += 1
                    role_member["operator"] += 1
                elif isinstance(member, Mentalist):
                    role_member["mentalist"] += 1

        average_experience = (
            (total_experience / operator_count) if operator_count > 0 else 0
        )

        return {
            "nombre_de_vaisseaux": len(self.__spaceships),
            "moyenne_experience_operator": average_experience,
            "repartition_roles": role_member,
            "total_membres": total_members,
        }
