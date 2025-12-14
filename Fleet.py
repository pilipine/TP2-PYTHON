# Fleet.py
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship

ALLOWED_SHIP_TYPES = {"Marchand", "Guerre", "Exploration"}
ALLOWED_CONDITIONS = {"Opérationnel", "Endommagé"}


class Fleet:
    def __init__(self, name, spaceships=None):
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
        """
        Ajoute un vaisseau après validations.
        Retourne True si ajouté, False sinon.
        """
        # Vérifier que ship a les méthodes nécessaires
        required_methods = ("get_name", "get_ship_type", "get_condition")
        if not all(
            hasattr(ship, m) and callable(getattr(ship, m)) for m in required_methods
        ):
            print("[ERR] Doit être un objet de type Spaceship (méthodes manquantes).")
            return False

        # Capacité
        if len(self.__spaceships) >= 15:
            print("[WARN] Capacité max de 15 vaisseaux atteinte.")
            return False

        # Unicité (optionnel)
        ship_name = ship.get_name()
        if any(
            s.get_name().strip().lower() == ship_name.strip().lower()
            for s in self.__spaceships
        ):
            print(f"[INFO] Un vaisseau nommé '{ship_name}' existe déjà dans la flotte.")
            return False

        # Validation type
        ship_type = ship.get_ship_type()
        if not ship_type or ship_type.strip() == "":
            print("[ERR] Type de vaisseau manquant.")
            return False
        type_norm = ship_type.strip().capitalize()
        if type_norm not in ALLOWED_SHIP_TYPES:
            print(
                f"[ERR] Type invalide: '{ship_type}'. "
                f"Valeurs autorisées: {', '.join(sorted(ALLOWED_SHIP_TYPES))}."
            )
            return False

        # Validation état
        condition = ship.get_condition()
        if not condition or condition.strip() == "":
            print("[ERR] État du vaisseau manquant.")
            return False
        cond_norm = condition.lower().replace("é", "e")
        if cond_norm == "operationnel":
            condition = "Opérationnel"
        elif cond_norm == "endommage":
            condition = "Endommagé"
        if condition not in ALLOWED_CONDITIONS:
            print(
                f"[ERR] État invalide: '{condition}'. "
                f"Valeurs autorisées: {', '.join(sorted(ALLOWED_CONDITIONS))}."
            )
            return False

        # Ajout
        self.__spaceships.append(ship)
        print(f"[OK] '{ship.get_name()}' ajouté à la flotte '{self.get_name()}'.")
        return True

    # --------- Aliases pour compatibilité ----------
    def add_ship(self, ship):
        return self.append_ship(ship)

    def append_spaceship(self, ship):
        return self.append_ship(ship)

    # --------- Statistiques ----------
    def statistics(self):
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


# --------- Choix d'un vaisseau (fonction utilitaire, hors classe) ----------
def choose_ship(fleet):
    """Sélection simple dans une liste de vaisseaux ou un objet Fleet."""
    items = fleet.get_spaceships() if isinstance(fleet, Fleet) else fleet

    if not items:
        print("Aucun vaisseau disponible.")
        return None

    print("\nListe des vaisseaux :")
    for i, s in enumerate(items, start=1):
        print(f"{i}. {s.get_name()} ({s.get_ship_type()})")

    raw = input("Choisissez un numéro (Enter pour annuler) : ").strip()
    if not raw:
        return None
    if not raw.isdigit():
        print("Entrée invalide.")
        return None

    idx = int(raw)
    if not (1 <= idx <= len(items)):
        print("Numéro hors plage.")
        return None

    return items[idx - 1]
