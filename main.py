# main.py
from Member import *
from Operator import *
from Mentalist import Mentalist, MAX_MANA
from Spaceship import *
from Fleet import *

# Instanciation de la classe Staceship (Créer un vaisseau)
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


print("\n--- Équipage du vaisseau Bayta ---")
for member in bayta.get_crew():
    member.introduce_yourself()
for member in dark_nebula.get_crew():
    member.introduce_yourself()
for member in fearless.get_crew():
    member.introduce_yourself()


# Le mentaliste influence un opérateur
Tellem_Bond.act(Gaal_Dornick)
Yanna_Seldon.act(Hugo_Crast)
Joie.act(Hugo_Crast)

# supprime un membre de l'équipage
bayta.remove_member("Dornick")

# Afficher équipage
bayta.display_crew()

# Vérifier préparation
if bayta.check_preparation():
    print("Le vaisseau est pret à décoller.")
else:
    print("Le vaisseau n'est pas prêt.")


def choose_ship_interactively(ships):
    """
    Demande à l'utilisateur de sélectionner un vaisseau par numéro.
    ships : liste d'objets Spaceship
    Retourne le vaisseau choisi ou None si erreur.
    """
    if not ships:
        print("[ERR] Aucun vaisseau disponible.")
        return None

    print("\n=== Sélection du vaisseau ===")
    for i, ship in enumerate(ships, start=1):
        print(f"{i}. {ship.get_name()} ({ship.get_ship_type()})")

    choice = input("Entrez le numéro du vaisseau : ").strip()
    if not choice.isdigit():
        print("[ERR] Merci d'entrer un numéro.")
        return None

    idx = int(choice)
    if idx < 1 or idx > len(ships):
        print("[ERR] Numéro invalide.")
        return None

    selected = ships[idx - 1]
    print(f"[INFO] Vous avez sélectionné : {selected.get_name()}")
    return selected


def interactive_remove_member_flow(ships):
    """
    1) L'utilisateur sélectionne un vaisseau (input) -> variable ship
    2) On affiche la liste des membres (display_crew_list) -> list[]
    3) On demande quel membre supprimer (input lastname) -> variable lastname
    4) On supprime avec remove_member(lastname)
    5) On affiche 'Nous avons supprimé ... du vaisseau ...' si c'est OK
    6) On vérifie en réaffichant la liste
    """
    # Étape 1 : choisir un vaisseau
    ship = choose_ship_interactively(ships)
    if ship is None:
        return

    # Étape 2 : afficher l'équipage sous forme de list[]
    names_before = ship.display_crew_list()

    # Si pas de membres, on s'arrête là
    if not names_before:
        return

    # Étape 3 : demander quel membre supprimer (par NOM DE FAMILLE)
    lastname = input("\nQuel membre allons-nous supprimer (NOM DE FAMILLE) ? ").strip()
    if not lastname:
        print("[ERR] Nom de famille vide.")
        return

    # Étape 4 : supprimer
    deleted = ship.remove_member(lastname)

    # Étape 5 : message utilisateur
    if deleted:
        print(f"\nNous avons supprimé '{lastname}' du vaisseau '{ship.get_name()}'.")
    else:
        print(f"\nAucun membre '{lastname}' n'a été supprimé dans '{ship.get_name()}'.")

    # Étape 6 : vérification (réafficher la liste et vérifier la présence du nom)
    names_after = ship.display_crew_list()
    if deleted:
        # Vérif simple : le lastname ne doit plus apparaître à la fin des noms
        still_here = any(n.split()[-1].lower() == lastname.lower() for n in names_after)
        if not still_here:
            print("[CHECK] Suppression vérifiée ")
        else:
            print(
                "[CHECK] Attention : un membre avec ce nom de famille est encore présent (homonymes ?)"
            )


# Regroupe tes vaisseaux dans une liste
ships = [bayta, dark_nebula, fearless, unimara, weinis]

# Lance le scénario interactif
interactive_remove_member_flow(ships)
