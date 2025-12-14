# main.py
from Member import *
from Operator import *
from Mentalist import Mentalist, MAX_MANA
from Spaceship import *
from Fleet import *
from save_load_json import *


# Instanciation de la classe Staceship
bayta = Spaceship("Bayta", "Marchand")
dark_nebula = Spaceship(
    name="Dark Nebula",
    ship_type="Guerre",
    crew=[],
    condition="Endommagé",
)
fearless = Spaceship(
    name="Fearless",
    ship_type="Guerre",
)
unimara = Spaceship(
    name="Unimara",
    ship_type="Marchand",
)
weinis = Spaceship(name="Weinis", ship_type="Marchand", crew=[], condition="Endommagé")

# Instancier de nouveaux membres d'équipage (Operators)
Bel_riose = Operator("Bel", "Riose", "Homme", 48, "commandant", experience=0)
Bel_riose.introduce_yourself()
Bel_riose.act()

Gaal_Dornick = Operator("Gaal", "Dornick", "Femme", 34, "technicien", experience=0)
Gaal_Dornick.introduce_yourself()
Gaal_Dornick.act()

Salvor_Hardin = Operator("Salvor", "Hardin", "Femme", 28, "armurier", experience=0)
Salvor_Hardin.introduce_yourself()
Salvor_Hardin.act()

Hugo_Crast = Operator("Hugo", "Crast", "Homme", 37, "pilote", experience=0)
Hugo_Crast.introduce_yourself()
Hugo_Crast.act()

# Instancier de nouveaux membres d'équipage (mentalistes)
Tellem_Bond = Mentalist("Tellem", "Bond", "Homme", 48, MAX_MANA)
print(f"Mana de départ est de : {Tellem_Bond.get_mana()}")
Tellem_Bond.recharge_mana()
print(f"Après recharge, votre mana est de : {Tellem_Bond.get_mana()}")

Yanna_Seldon = Mentalist("Yanna", "Seldon", "Femme", 52, MAX_MANA)
print(f"Mana de départ est de : {Yanna_Seldon.get_mana()}")
Yanna_Seldon.recharge_mana()
print(f"Après recharge, votre mana est de : {Yanna_Seldon.get_mana()}")

Joie = Mentalist("Joie", "", "Femme", 25, MAX_MANA)
print(f"Mana de départ est de : {Joie.get_mana()}")
Joie.recharge_mana()
print(f"Après recharge, votre mana est de : {Joie.get_mana()}")

# Ajoute des membres au vaisseau (capacité max 10)
bayta.append_member(Bel_riose)
bayta.append_member(Gaal_Dornick)
bayta.append_member(Salvor_Hardin)

dark_nebula.append_member(Hugo_Crast)
dark_nebula.append_member(Tellem_Bond)

fearless.append_member(Yanna_Seldon)
fearless.append_member(Joie)

# Créer la flotte (selon la signature corrigée de Fleet)
fleet = Fleet("Galactica", [bayta, dark_nebula, fearless, unimara, weinis])

# Le mentaliste influence un opérateur
Tellem_Bond.act(Gaal_Dornick)
Yanna_Seldon.act(Hugo_Crast)
Joie.act(Hugo_Crast)


# ======= menu interactif =======
while True:
    print(f"\n=== Gestion de la flotte : {fleet.get_name()} ===")
    print("1. Renommer la flotte")
    print("2. Ajouter un vaisseau à la flotte")
    print("3. Ajouter un membre d'équipage")
    print("4. Supprimer un membre d'équipage")
    print("5. Afficher les informations d'un équipage")
    print("6. Vérifier la préparation d'un vaisseau")
    print("7. Sauvegarde de la flotte (JSON)")
    print("8. Charger une flotte (JSON)")
    print("9. Quitter")

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
        else:
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
        # Ajouter un membre dans un vaisseau choisi
        print("\n=== Ajouter un membre ===")
        ship = choose_ship(fleet)
        if ship is None:
            print("Aucun vaisseau sélectionné.")
            continue

        first_name = input("Prénom : ").strip()
        last_name = input("Nom : ").strip()
        gender = input("Genre (Homme/Femme) : ").strip()
        role = input("Rôle (ex: pilote, technicien...) : ").strip()
        age = int(input("Âge : ").strip() or 0)

        # ⚠️ adapte au constructeur de ta classe Operator
        new_member = Operator(first_name, last_name, gender, age, role, experience=0)
        ship.append_member(new_member)
        print(f"[OK] {first_name} {last_name} ajouté(e) à {ship.get_name()}.")

    elif choice == "4":
        # Supprimer un membre
        ship = choose_ship(fleet)
        if ship is None:
            print("Aucun vaisseau sélectionné.")
            continue

        last_name_to_remove = input(
            "Entrez le nom de famille du membre à supprimer : "
        ).strip()
        if ship.remove_member(last_name_to_remove):
            print(f"[OK] Membre '{last_name_to_remove}' supprimé de {ship.get_name()}.")
        else:
            print(
                f"[INFO] Aucun membre '{last_name_to_remove}' trouvé dans {ship.get_name()}."
            )

    elif choice == "5":
        # Afficher l'équipage d'un vaisseau choisi
        ship = choose_ship(fleet)
        if ship is None:
            print("Aucun vaisseau sélectionné.")
            continue
        print(f"\n--- Équipage de {ship.get_name()} ---")
        ship.display_crew()  # assure-toi que cette méthode existe

    elif choice == "6":
        ship = choose_ship(fleet)
        if ship is None:
            print("Aucun vaisseau sélectionné.")
            continue
        ready, msg = ship.check_preparation()  
        print(msg)

    elif choice == "7":
        # Sauvegarder la flotte courante dans un fichier JSON
        file_name = (
            input("Nom du fichier JSON (ex: data/fleet.json): ").strip()
            or "data/fleet.json"
        )
        try:
            save_data(fleet, file_name)
            print(f" Flotte sauvegardée dans {file_name}")
        except Exception as e:
            print(f" Erreur de sauvegarde: {e}")

    
    elif choice == "8":
        file_name = input("Nom du fichier JSON à charger (ex: data/fleet.json): ").strip() or "data/fleet.json"
        try:
            fleet = load_data(file_name)  # on remplace la flotte courante
            print(f" Flotte chargée depuis {file_name}")
        except Exception as e:
            print(f" Erreur de chargement: {e}")


    elif choice == "9":
        print("Au revoir !")
        break

    else:
        print("[ERR] Option invalide.")
