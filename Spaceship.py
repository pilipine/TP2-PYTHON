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

    def remove_member(self, last_name):
        """
        Supprime le premier membre dont le nom de famille (last_name) correspond.
        Retourne True si supprimé, False sinon.
        """
        target = str(last_name).strip().lower()
        for i, m in enumerate(self.__crew):
            # Récupère le last_name via getter si dispo, sinon attribut direct
            lname = (
                m.get_last_name()
                if hasattr(m, "get_last_name")
                else getattr(m, "lastname", "") or ""
            )
            if str(lname).strip().lower() == target:
                removed = self.__crew.pop(i)
                # Affiche confirmation
                fname = (
                    removed.get_first_name()
                    if hasattr(removed, "get_first_name")
                    else getattr(removed, "firstname", "")
                )
                print(
                    f"[OK] {fname} {lname} a été supprimé de l'équipage du vaisseau {self.get_name()}."
                )
                return True
        print(
            f"[INFO] Aucun membre avec le nom de famille '{last_name}' n'a été trouvé dans l'équipage de {self.get_name()}."
        )
        return False

    def display_crew(self):
        print(
            f"\n--- Équipage du vaisseau {self.get_name()} ({self.get_ship_type()}) ---"
        )
        if not self.__crew:
            print("(aucun membre)")
            return

        for m in self.__crew:
            # Récupération des champs de base avec getters ou attributs
            fname = (
                m.get_first_name()
                if hasattr(m, "get_first_name")
                else getattr(m, "firstname", "")
            )
            lname = (
                m.get_last_name()
                if hasattr(m, "get_last_name")
                else getattr(m, "lastname", "")
            )
            gender = (
                m.get_gender() if hasattr(m, "get_gender") else getattr(m, "gender", "")
            )
            age = m.get_age() if hasattr(m, "get_age") else getattr(m, "age", "")

            # Cas spécifique selon le type
            if isinstance(m, Operator):
                role = (
                    m.get_role()
                    if hasattr(m, "get_role")
                    else getattr(m, "role", "membre")
                )
                article = "un"
                if self.__gender.lower() == "femme":
                    article = "une"
                print(
                    f"- {fname} {lname} est un.e {gender.lower()} de {age} ans au rôle de {role}."
                )
            elif isinstance(m, Mentalist):
                mana = m.get_mana() if hasattr(m, "get_mana") else getattr(m, "mana", 0)
                print(
                    f"- {fname} {lname} est {article} {gender.lower()} de {age} ans avec {mana} de mana."
                )
            else:
                # Autres types éventuels héritant de Member
                print(
                    f"- {fname} {lname} est un.e {gender.lower()} de {age} ans (membre d’équipage)."
                )

    def check_preparation(self):
        """
        Vérifie qu'au moins un pilote et un technicien sont présents à bord.
        Retourne True si le vaisseau est prêt, sinon False.
        """
        has_pilot = False
        has_technician = False

        for m in self.__crew:
            # On ne s'intéresse qu'aux Operators (les Mentalists n'ont pas de rôle métier)
            if isinstance(m, Operator):
                # Récupération du rôle via getter si dispo, sinon attribut
                role = (
                    m.get_role()
                    if hasattr(m, "get_role")
                    else getattr(m, "role", "") or ""
                )
                r = str(role).strip().lower()

                # Normalisation simple : accepte 'pilote' et 'technicien'
                if r == "pilote":
                    has_pilot = True
                elif r == "technicien":
                    has_technician = True

                # Early exit si les deux sont déjà trouvés
                if has_pilot and has_technician:
                    return True

        # Si on sort de la boucle sans avoir les deux rôles requis
        return False
