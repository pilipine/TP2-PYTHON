
# fleet.py
from typing import List, Dict
from Spaceship import Spaceship
from operator import Operator
from Mentalist import Mentalist
from Member import Member


class Fleet:
    """
    Modélise une flotte de vaisseaux.

    Attributs :
      - name (str)                : nom de la flotte
      - spaceships (list[Spaceship]) : liste des vaisseaux (initialisée vide)

    Méthodes :
      - append_spaceship(spaceship: Spaceship) -> bool
          Ajoute un vaisseau si la capacité max (15) n'est pas dépassée et si l'objet est valide.
      - statistics() -> dict
          Calcule des infos sur la flotte :
            * nombre total de vaisseaux
            * nombre total de membres
            * répartition des rôles (operators)
            * moyenne d'expérience des opérateurs
            * nombre de mentalistes et mentalistes avec mana >= 50
      - display() -> None
          Affiche un aperçu de la flotte et des vaisseaux.
    """

    def __init__(self, name: str):
        self.name = name
        self.spaceships: List[Spaceship] = []

    # ---------- Ajout d'un vaisseau ----------
    def append_spaceship(self, spaceship: Spaceship) -> bool:
        """Ajoute un vaisseau si la capacité (15) n'est pas dépassée et si le type est valide."""
        if not isinstance(spaceship, Spaceship):
            print("[WARN] Seuls des objets Spaceship sont autorisés dans la flotte.")
            return False

        if len(self.spaceships) >= 15:
            print("[WARN] Capacité maximale de 15 vaisseaux atteinte pour la flotte.")
            return False

        self.spaceships.append(spaceship)
        print(f"[INFO] Le vaisseau '{spaceship.name}' a rejoint la flotte '{self.name}'.")
        return True

    # ---------- Statistiques globales ----------
    def statistics(self) -> Dict[str, object]:
        """
        Retourne un dictionnaire d'informations agrégées sur la flotte
        et affiche un résumé lisible en console.
        """
        total_vessels = len(self.spaceships)
        total_members = 0

        role_distribution: Dict[str, int] = {}
        operator_count = 0
        operator_xp_sum = 0

        mentalist_count = 0
        mentalist_50_count = 0

        for ship in self.spaceships:
            total_members += len(ship.crew)

            for m in ship.crew:
                # ---- Opérateurs ----
                if isinstance(m, Operator):
                    operator_count += 1

                    # Rôle (via getter ou attribut)
                    role = m.get_role() if hasattr(m, "get_role") else getattr(m, "role", "")
                    role = (role or "").lower()
                    role_distribution[role] = role_distribution.get(role, 0) + 1

                    # Expérience
                    xp = m.get_experience() if hasattr(m, "get_experience") else getattr(m, "experience", 0)
                    operator_xp_sum += int(xp)

                # ---- Mentalistes ----
                if isinstance(m, Mentalist):
                    mentalist_count += 1
                    mana = m.get_mana() if hasattr(m, "get_mana") else getattr(m, "mana", 0)
                    if mana >= 50:
                        mentalist_50_count += 1

        operator_xp_avg = (operator_xp_sum / operator_count) if operator_count > 0 else 0.0

        stats = {
            "fleet_name": self.name,
            "total_vessels": total_vessels,
            "total_members": total_members,
            "role_distribution": role_distribution,
            "operator_count": operator_count,
            "operator_experience_avg": round(operator_xp_avg, 2),
            "mentalists": mentalist_count,
            "mentalists_mana_50_plus": mentalist_50_count,
        }

        # Affichage lisible (optionnel)
        print(f"\n=== Statistiques de la flotte '{self.name}' ===")
        print(f"Vaisseaux : {total_vessels}")
        print(f"Membres   : {total_members}")
        print(f"Opérateurs: {operator_count} | XP moyenne: {stats['operator_experience_avg']}")
        print(f"Répartition des rôles : {role_distribution}")
        print(f"Mentalistes : {mentalist_count} | Mana ≥ 50 : {mentalist_50_count}")
        print("=============================================\n")

        return stats

    # ---------- Affichage d'ensemble ----------
    def display(self) -> None:
        """Affiche un aperçu de la flotte et de ses vaisseaux."""
        if not self.spaceships:
            print(f"La flotte '{self.name}' ne contient aucun vaisseau.")
            return

        print(f"--- Flotte '{self.name}' ---")
        for ship in self.spaceships:
            print(f"* {ship.name} ({ship.shipType}, {ship.condition}) - Équipage: {len(ship.crew)}")
        print("----------------------------")
