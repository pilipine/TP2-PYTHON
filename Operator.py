from Member import *


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

    def introduce_yourself(self):
        super().introduce_yourself()
        print(
            f"Mon rôle est : {self.get_role()} et mon expérience est de :{  self.get_experience()}"
        )


# ==== Mission Galactique – Helpers ====


def _is_operator(m):
    return m.__class__.__name__.lower() == "operator"


def _is_mentalist(m):
    return m.__class__.__name__.lower() == "mentalist"


def _safe_get(obj, getter_name, attr_name, default=None):
    """Récupère une valeur via getter() si présent, sinon via l'attribut."""
    if hasattr(obj, getter_name) and callable(getattr(obj, getter_name)):
        try:
            return getattr(obj, getter_name)()
        except Exception:
            pass
    return getattr(obj, attr_name, default)


def _safe_set(obj, setter_name, attr_name, value):
    """Affecte une valeur via setter(val) si présent, sinon via l'attribut."""
    if hasattr(obj, setter_name) and callable(getattr(obj, setter_name)):
        try:
            getattr(obj, setter_name)(value)
            return True
        except Exception:
            pass
    try:
        setattr(obj, attr_name, value)
        return True
    except Exception:
        return False


def _get_role(op):
    return _safe_get(op, "get_role", "role", "").lower()


def _get_mana(mentalist):
    return _safe_get(mentalist, "get_mana", "mana", None)


def _set_mana(mentalist, value):
    _safe_set(mentalist, "set_mana", "mana", value)


def _get_ship_name(ship):
    return _safe_get(ship, "get_name", "name", "???")


def _get_ship_condition(ship):
    return _safe_get(ship, "get_condition", "condition", "Opérationnel")


def _set_ship_condition(ship, value):
    _safe_set(ship, "set_condition", "condition", value)


def mission_ready(ship):
    """
    Règles de préparation pour une mission réussie :
    - au moins 1 pilote
    - au moins 1 technicien
    - au moins 1 mentaliste avec mana >= 50 (consommé à la réussite)
    Retourne (ready: bool, mentalist_ok: Mentalist|None)
    """
    has_pilot = False
    has_technician = False
    mentalist_ok = None

    for member in getattr(ship, "crew", []):
        if _is_operator(member):
            role = _get_role(member)
            if role == "pilote":
                has_pilot = True
            elif role == "technicien":
                has_technician = True
        elif _is_mentalist(member) and mentalist_ok is None:
            mana = _get_mana(member)
            if mana is not None and mana >= 50:
                mentalist_ok = member

    return (has_pilot and has_technician and mentalist_ok is not None), mentalist_ok


def _gain_experience(op, n=1):
    """+n d'XP : utilise gain_experience() si dispo, sinon incrémente l'attribut."""
    if hasattr(op, "gain_experience") and callable(getattr(op, "gain_experience")):
        for _ in range(n):
            try:
                op.gain_experience()
            except Exception:
                break
    else:
        try:
            current = getattr(op, "experience", 0)
            setattr(op, "experience", current + n)
        except Exception:
            pass


def run_mission(ship):
    """Exécute la mission galactique pour un vaisseau."""
    name = _get_ship_name(ship)
    print(f"\n=== 🚀 Mission Galactique – {name} ===")

    ready, mentalist = mission_ready(ship)
    if not ready:
        print(
            "⛔ Mission impossible : il faut au moins un pilote, un technicien "
            "et un mentaliste avec ≥ 50 mana."
        )
        _set_ship_condition(ship, "Endommagé")
        print(f"⚠️  {name} a été endommagé pendant la tentative.")
        return

    # Mission réussie (règle demandée)
    print("✅ Conditions remplies : la mission RÉUSSIT !")

    # Consomme 50 mana du mentaliste participant
    mana_before = _get_mana(mentalist)
    if mana_before is not None:
        _set_mana(mentalist, max(0, mana_before - 50))
        mana_after = _get_mana(mentalist)
        first = _safe_get(mentalist, "get_first_name", "first_name", "Le mentaliste")
        print(f"🧠 Mana consommé : {first} passe de {mana_before} → {mana_after}")

    # +1 XP pour tous les opérateurs du vaisseau
    gained = 0
    for member in getattr(ship, "crew", []):
        if _is_operator(member):
            _gain_experience(member, 1)
            gained += 1
    print(f"🎖️ Expérience +1 pour {gained} opérateur(s).")

    # Le vaisseau est opérationnel en fin de mission
    _set_ship_condition(ship, "Opérationnel")
    print(f"🛠️  État du vaisseau : {_get_ship_condition(ship)}")
