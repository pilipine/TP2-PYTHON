# spaceship.py
# Imports des classes
from Member import Member
from Operator import Operator
from Mentalist import Mentalist


class Spaceship:
    def __init__(self, name, ship_type, crew=None, condition="Opérationnel"):
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = list(crew) if crew is not None else []
        self.__condition = condition

    # --------- Getter/Setter mana ----------
    def get_name(self):
        return self.__name

    def get_ship_type(self):
        return self.__ship_type

    def get_crew(self):
        return list(self.__crew)

    def get_condition(self):
        return self.__condition

    def set_name(self, new_name):
        self.__name = new_name

    def set_ship_type(self, new_ship_type):
        self.__ship_type = new_ship_type

    def set_crew(self, new_crew):
        # idéalement : vérifier que tous les éléments sont des Member
        if not all(isinstance(m, Member) for m in new_crew):
            raise TypeError(
                "Tous les éléments de l'équipage doivent hériter de Member."
            )
        self.__crew = list(new_crew)

    def set_condition(self, new_condition):
        self.__condition = new_condition

    # Méthodes classe Spaceship

    def append_member(self, member):
        # Capacité
        if len(self.__crew) >= 10:
            print("[WARN] Capacité max de 10 membres déjà atteinte.")
            return False

        # Type attendu : toute sous-classe de Member (Operator, Mentalist, etc.)
        if not isinstance(member, Member):
            print("[ERR] Le membre doit hériter de Member (Operator, Mentalist, ...).")
            return False

        # Ajout + message
        self.__crew.append(member)

        # Récupération prénom/nom via getters si dispo, sinon attributs
        fname = (
            member.get_first_name()
            if hasattr(member, "get_first_name")
            else getattr(member, "firstname", "")
        )
        lname = (
            member.get_last_name()
            if hasattr(member, "get_last_name")
            else getattr(member, "lastname", "")
        )
        print(f"Bienvenue à bord, {fname} {lname} du vaisseau {self.get_name()} !")
        return True

    # --- Supprimer un membre par NOM DE FAMILLE (lastname) ---
    def remove_member(self, lastname: str) -> bool:
        """
        Supprime le PREMIER membre trouvé dont le nom de famille correspond (insensible à la casse).
        Utilise list.remove() pour retirer l'objet exact.
        Retourne True si suppression faite, sinon False.
        """
        # 1) Trouver l'objet membre à supprimer
        to_remove = None
        for m in self.__crew:
            if m.lastname.lower() == lastname.lower():
                to_remove = m
                break

        # 2) Si trouvé → utiliser list.remove(objet)
        if to_remove is not None:
            self.__crew.remove(to_remove)  # <- méthode remove()
            print(
                f"[OK] {to_remove.firstname} {to_remove.lastname} a été supprimé du vaisseau {self.get_name()}."
            )
            return True

        # 3) Sinon informer
        print(
            f"[INFO] Aucun membre avec le nom '{lastname}' trouvé dans {self.get_name()}."
        )
        return False

    # --- Variante interactive (demande le nom via input) ---
    def remove_member_input(self) -> bool:
        """
        Demande à l'utilisateur le NOM DE FAMILLE à supprimer puis appelle remove_member().
        """
        lastname = input(
            "Quel est le NOM DE FAMILLE (lastname) du membre à supprimer ? "
        ).strip()
        if not lastname:
            print("[ERR] Le nom de famille ne peut pas être vide.")
            return False

    # def check_preparation(self):
    # has_pilot = False
    # has_technician = False

    # for member in self.get_crew():
    # if hasattr(member, "get_role"):  # Vérifie que le membre a un rôle
    # role = member.get_role().lower()
    # if role == "pilote":
    # has_pilot = True
    # elif role == "technicien":
    # has_technician = True

    # Si les deux sont trouvés
    # if has_pilot and has_technician:
    # return True

    # Après la boucle, on retourne True seulement si les deux sont présents
    # if has_pilot and has_technician:
    # return True
    # else:
    # return False
