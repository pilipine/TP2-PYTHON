import json
import ast


def save_data(fleet, file_name):
    # 1. Convertir l'objet en chaîne JSON
    json_string = json.dumps(
        fleet, default=lambda o: o.__dict__, sort_keys=True, indent=4
    )

    # 2. Convertir la chaîne en dictionnaire
    json_dict = ast.literal_eval(json_string)

    # 3. Enregistrer le dictionnaire dans un fichier JSON
    with open(file_name, "w") as file:
        json.dump(json_dict, file)


# main.py
from Member import *
from Operator import *
from Mentalist import Mentalist, MAX_MANA
from Spaceship import *
from Fleet import *

# ---------- Instanciation des vaisseaux ----------
bayta = Spaceship("Bayta", "Marchand")
dark_nebula = Spaceship(
    name="Dark Nebula",
    ship_type="Guerre",
    crew=[],
    condition="Endommagé",
)
fearless = Spaceship(name="Fearless", ship_type="Guerre")
unimara = Spaceship(name="Unimara", ship_type="Marchand")
weinis = Spaceship(name="Weinis", ship_type="Marchand", crew=[], condition="Endommagé")

# ---------- Équipage (Operators) ----------
Bel_riose = Operator("Bel", "Riose", "Homme", 48, "commandant", experience=0)
Gaal_Dornick = Operator("Gaal", "Dornick", "Femme", 34, "technicien", experience=0)
Salvor_Hardin = Operator("Salvor", "Hardin", "Femme", 28, "armurier", experience=0)
Hugo_Crast = Operator("Hugo", "Crast", "Homme", 37, "pilote", experience=0)

# (tu peux garder ces lignes si tu veux leurs sorties)
Bel_riose.introduce_yourself()
Bel_riose.act()
Gaal_Dornick.introduce_yourself()
Gaal_Dornick.act()
Salvor_Hardin.introduce_yourself()
Salvor_Hardin.act()
Hugo_Crast.introduce_yourself()
Hugo_Crast.act()

# ---------- Équipage (Mentalists) ----------
Tellem_Bond = Mentalist("Tellem", "Bond", "Homme", 48, MAX_MANA)
Yanna_Seldon = Mentalist("Yanna", "Seldon", "Femme", 52, MAX_MANA)
Joie = Mentalist("Joie", "", "Femme", 25, MAX_MANA)

print(f"Mana de départ est de : {Tellem_Bond.get_mana()}")
Tellem_Bond.recharge_mana()
print(f"Après recharge, votre mana est de : {Tellem_Bond.get_mana()}")
print(f"Mana de départ est de : {Yanna_Seldon.get_mana()}")
Yanna_Seldon.recharge_mana()
print(f"Après recharge, votre mana est de : {Yanna_Seldon.get_mana()}")
print(f"Mana de départ est de : {Joie.get_mana()}")
Joie.recharge_mana()
print(f"Après recharge, votre mana est de : {Joie.get_mana()}")

# ---------- Affectation des membres aux vaisseaux ----------
bayta.append_member(Bel_riose)
bayta.append_member(Gaal_Dornick)
bayta.append_member(Salvor_Hardin)

dark_nebula.append_member(Hugo_Crast)
dark_nebula.append_member(Tellem_Bond)

fearless.append_member(Yanna_Seldon)
fearless.append_member(Joie)

# ---------- Création de la flotte (UNE SEULE FOIS) ----------
fleet = Fleet("Galactica", [bayta, dark_nebula, fearless, unimara, weinis])

# ---------- Actions des mentalistes ----------
Tellem_Bond.act(Gaal_Dornick)
Yanna_Seldon.act(Hugo_Crast)
Joie.act(Hugo_Crast)


# ---------- UI ----------
def afficher_menu(fleet: Fleet):
    print(f"\n=== Gestion de la flotte : {fleet.get_name()} ===")
    print("1. Renommer la flotte")
    print("2. Ajouter un vaisseau à la flotte")
    print("3. Ajouter un membre d'équipage")
    print("4. Supprimer un membre d'équipage")
    print("5. Afficher les informations d'un équipage")
    print("6. Vérifier la préparation d'un vaisseau")
    print("7. Quitter")


def choose_ship(fleet: Fleet):
    """Sélectionne un vaisseau par son index dans la flotte.
    Ajuste selon l'API de ta classe Fleet (get_ships, etc.)."""
    ships = (
        fleet.get_ships()
        if hasattr(fleet, "get_ships")
        else getattr(fleet, "_ships", [])
    )
    if not ships:
        print("[INFO] Aucun vaisseau dans la flotte.")
        return None
    print("\n--- Sélection du vaisseau ---")
    for i, s in enumerate(ships, start=1):
        print(f"{i}. {s.get_name()}")
    try:
        idx = int(input("Entrez le numéro : ").strip())
        return ships[idx - 1] if 1 <= idx <= len(ships) else None
    except ValueError:
        return None


def run_menu():
    while True:
        afficher_menu(fleet)
        choice = input("Choisissez une option : ").strip()

        if choice == "1":
            # Renommer la flotte
            print(f"\nNom actuel de la flotte : {fleet.get_name()}")
            new_name = input("Nouveau nom de la flotte : ").strip()
            if not new_name:
                print("[INFO] Nom inchangé (entrée vide).")
            else:
                fleet.set_name(new_name)
                print(f"[OK] La flotte s'appelle maintenant : {fleet.get_name()}")

        elif choice == "2":
            print("\n=== Ajouter un vaisseau à la flotte ===")
            name = input("Nom du vaisseau : ").strip()
            if not name:
                print("[ERR] Le nom du vaisseau est obligatoire.")
                continue
            ship_type = (
                input("Type (ex: Marchand, Guerre, Exploration) : ").strip()
                or "Marchand"
            )
            condition = (
                input("État (Opérationnel/Endommagé) [défaut: Opérationnel] : ").strip()
                or "Opérationnel"
            )
            new_ship = Spaceship(name=name, ship_type=ship_type, condition=condition)
            if fleet.append_ship(new_ship):
                print(f"[OK] Vaisseau '{name}' ({ship_type}) ajouté.")
            else:
                print("[INFO] Ajout non effectué (capacité/validation).")

        elif choice == "3":
            print("\n=== Ajouter un membre ===")
            first_name = input("Prénom : ").strip()
            last_name = input("Nom : ").strip()
            role = input("Rôle (ex: pilote, technicien...) : ").strip()
            try:
                age = int(input("Âge : ").strip() or 0)
            except ValueError:
                print("[ERR] Âge invalide.")
                continue
            new_member = Operator(
                first_name, last_name, "Homme/Femme", age, role, experience=0
            )
            ship = choose_ship(fleet)
            if ship is None:
                print("[ERR] Choix de vaisseau invalide.")
                continue
            ship.append_member(new_member)
            print(f"[OK] Membre ajouté à {ship.get_name()}.")

        elif choice == "4":
            ship = choose_ship(fleet)
            if ship is None:
                print("[ERR] Choix de vaisseau invalide.")
                continue
            last_name_to_remove = input(
                "Entrez le nom de famille du membre à supprimer : "
            ).strip()
            if ship.remove_member(last_name_to_remove):
                print(f"[OK] '{last_name_to_remove}' supprimé de {ship.get_name()}.")
            else:
                print(
                    f"[INFO] Aucun membre nommé '{last_name_to_remove}' dans {ship.get_name()}."
                )

        elif choice == "5":
            print("\n>>> Vérification de l'affichage des équipages :")
            for s in (bayta, dark_nebula, fearless, unimara, weinis):
                s.display_crew()

        elif choice == "6":
            ship = choose_ship(fleet)
            if ship is None:
                print("[ERR] Choix de vaisseau invalide.")
                continue
            ready, msg = ship.check_preparation()
            print(msg)

        elif choice == "7":
            print("Au revoir !")
            break

        else:
            print("[ERR] Option invalide.")


if __name__ == "__main__":
    run_menu()
