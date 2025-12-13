# main.py
from Member import *
from Operator import *
from Mentalist import Mentalist, MAX_MANA
from Spaceship import *
from Fleet import *


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


# --- Choisir le vaisseau ciblé ---
print("\nSur quel vaisseau voulez-vous agir ?")
print("1. Bayta\n2. Dark Nebula\n3. Fearless\n4. Unimara\n5. Weinis")
choice = input("Entrez le numéro : ").strip()

ship = None
if choice == "1":
    ship = bayta
elif choice == "2":
    ship = dark_nebula
elif choice == "3":
    ship = fearless
elif choice == "4":
    ship = unimara
elif choice == "5":
    ship = weinis
else:
    print("[ERR] Choix invalide.")
    ship = None


# ======= menu interactif =======
while True:
    print("\n=== Gestion de la flotte : Galactica ===")
    print("1. Renommer la flotte")
    print("2. Ajouter un vaisseau à la flotte")
    print("3. Ajouter un membre d'équipage")
    print("4. Supprimer un membre d'équipage")
    print("5. Afficher les informations d'un équipage")
    print("6. Vérifier la préparation d'un vaisseau")
    print("7. Quitter")

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
        if fleet.append_ship(new_ship):  # alias add_ship si tu préfères
            print(f"[OK] Vaisseau '{name}' ({ship_type}) ajouté.")
        else:
            print("[INFO] Ajout non effectué (capacité/validation).")

    elif choice == "3":
        # Ajoute des membres au vaisseau (capacité max 10)

        print("\n=== Ajouter un membre ===")
        first_name = input("Prénom : ").strip()
        last_name = input("Nom : ").strip()
        role = input("Rôle (ex: pilote, technicien...) : ").strip()
        age = int(input("Âge : ").strip() or 0)
        new_member = Operator(
            first_name, last_name, "Homme/Femme", age, role, experience=0
        )

        print("\nDans quel vaisseau ajouter ce membre ?")
        print("1. Bayta\n2. Dark Nebula\n3. Fearless\n4. Unimara\n5. Weinis")
        choice = input("Entrez le numéro : ").strip()

        if choice == "1":
            bayta.append_member(new_member)
        elif choice == "2":
            dark_nebula.append_member(new_member)
        elif choice == "3":
            fearless.append_member(new_member)
        elif choice == "4":
            unimara.append_member(new_member)
        elif choice == "5":
            weinis.append_member(new_member)
        else:
            print("[ERR] Choix invalide.")

        print("\n--- Équipage du vaisseau Bayta ---")
        for member in bayta.get_crew():
            member.introduce_yourself()
        for member in dark_nebula.get_crew():
            member.introduce_yourself()
        for member in fearless.get_crew():
            member.introduce_yourself()

    elif choice == "4":
        # Supprimer un membre
        if ship is not None:
            last_name_to_remove = input(
                "Entrez le nom de famille du membre à supprimer : "
            ).strip()
        if ship.remove_member(last_name_to_remove):
            print(
                f"Le membre avec le nom '{last_name_to_remove}' a bien été supprimé de {ship.get_name()}."
            )
        else:
            print(
                f"Aucun membre avec le nom '{last_name_to_remove}' n'a été trouvé dans {ship.get_name()}."
            )

    elif choice == "5":
        # Afficher équipage
        print("\n>>> Vérification de l'affichage des équipages :")
        bayta.display_crew()
        dark_nebula.display_crew()
        fearless.display_crew()
        unimara.display_crew()
        weinis.display_crew()

    elif choice == "6":
        # Vérifier préparation
        if ship.check_preparation():
            print(f"{ship.get_name()} est prêt à partir !")
        else:
            print(f"{ship.get_name()} n’est pas prêt.")

    elif choice == "7":
        print("Au revoir !")
        break

    else:
        print("[ERR] Option invalide.")
