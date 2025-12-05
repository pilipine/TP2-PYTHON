
# spaceship.py
# Imports des classes (assure-toi que les noms de fichiers sont en minuscules : member.py, operator.py, mentalist.py)
from Member import Member
from Operator import Operateur
from Mentalist import Mentalist


class Spaceship:
    """
    Modélise un vaisseau avec :
      - name (str)       : nom du vaisseau
      - shipType (str)   : type ('transport', 'guerre', 'marchand', etc.)
      - condition (str)  : état ('opérationnel', 'endommagé', ...)
      - crew (list[Member]) : liste d'objets (Member/Operator/Mentalist), initialisée vide

    Méthodes (exigences du TP) :
      - append_member(member: Member) -> bool
          Ajoute un membre si :
            * member est une instance de Member/Operator/Mentalist
            * la capacité max (10) n'est pas dépassée
      - remove_member(last_name: str) -> bool
          Supprime le premier membre dont le nom de famille correspond (ou False si introuvable)
      - display_crew() -> None
          Affiche une présentation de chaque membre (+ rôle si Operator, + mana si Mentalist)
      - check_preparation() -> bool
          Vérifie qu'il y a au moins :
            * un pilote
            * un technicien
            * (bonus TP) un mentaliste avec mana >= 50
    """

    def __init__(self, name: str, shipType: str, condition: str = "opérationnel"):
        self.name = name
        self.shipType = shipType
        self.condition = condition
        self.crew: list[Member] = []

    # ---------- Ajout ----------
    def append_member(self, member: Member) -> bool:
        """Ajoute un membre si la capacité (10) n'est pas dépassée et si le type est valide."""
        if not isinstance(member, Member):
            print("[WARN] Seuls des objets Member/Operator/Mentalist sont autorisés.")
            return False
        if len(self.crew) >= 10:
            print("[WARN] Capacité maximale de 10 membres atteinte.")
            return False

        self.crew.append(member)
        print(f"[INFO] {member.first_name} {member.last_name} rejoint {self.name}.")
        return True

    # ---------- Suppression ----------
    def remove_member(self, last_name: str) -> bool:
        """
        Supprime le premier membre dont le nom de famille correspond.
        Retourne True si supprimé, sinon False et affiche un message.
        """
        for i, m in enumerate(self.crew):
            # selon ta classe Member : first_name/last_name publics ou getters ?
            ln = getattr(m, "last_name", None) or getattr(m, "get_last_name", lambda: None)()
            if ln and ln.lower() == last_name.strip().lower():
                removed = self.crew.pop(i)
                print(f"[INFO] {removed.first_name} {removed.last_name} a été retiré de {self.name}.")
                return True

        print(f"[WARN] Aucun membre avec le nom de famille '{last_name}' à bord de {self.name}.")
        return False

    # ---------- Affichage ----------
    def display_crew(self) -> None:
        """Affiche les informations détaillées de chaque membre."""
        if not self.crew:
            print(f"{self.name} n'a pas encore d'équipage.")
            return

        print(f"--- Équipage du {self.name} ({self.shipType}, {self.condition}) ---")
        for m in self.crew:
            who = m.introduce_yourself()

            # Rôle si Operator
            role = ""
            if isinstance(m, Operateur):
                # selon implémentation : attribut privé ou getter
                role_val = getattr(m, "get_role", None)
                role = f" | Rôle: {role_val()}" if callable(role_val) else f" | Rôle: {getattr(m, 'role', 'n/a')}"

            # Mana si Mentalist
            mana = ""
            if isinstance(m, Mentalist):
                mana_val = getattr(m, "get_mana", None)
                mana_points = mana_val() if callable(mana_val) else getattr(m, "mana", None)
                mana = f" | Mana: {mana_points}"

            print(who + role + mana)

    # ---------- Préparation ----------
    def check_preparation(self) -> bool:
        """
        Retourne True si le vaisseau est prêt :
          - au moins un 'pilote'
          - au moins un 'technicien'
          - (bonus TP) au moins un Mentalist avec mana >= 50
        """
        has_pilot = False
        has_tech = False
        has_mentalist_50 = False

        for m in self.crew:
            if isinstance(m, Operateur):
                # récupérer le rôle via getter ou attribut
                role = m.get_role() if hasattr(m, "get_role") else getattr(m, "role", "")
                r = (role or "").lower()
                if r == "pilote":
                    has_pilot = True
                elif r == "technicien":
                    has_tech = True

            if isinstance(m, Mentalist):
                mana = m.get_mana() if hasattr(m, "get_mana") else getattr(m, "mana", 0)
                if mana >= 50:
                    has_mentalist_50 = True

        ready = has_pilot and has_tech and has_mentalist_50
        print(f"[CHECK] Préparation du {self.name} → "
              f"pilote: {has_pilot}, technicien: {has_tech}, mentaliste(≥50): {has_mentalist_50} | READY={ready}")
        return ready
