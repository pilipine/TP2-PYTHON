# main.py
from Member import *
from Operator import *
from Mentalist import Mentalist, MAX_MANA
from Spaceship import *
from Fleet import *

# Créer un vaisseau
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

# Instancier des mentalistes
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

# Ajoute des membres au vaisseau (capacité max 10)bayta.append_member(Bel_riose)
bayta.append_member(Gaal_Dornick)
bayta.append_member(Salvor_Hardin)
dark_nebula.append_member(Hugo_Crast)
dark_nebula.append_member(Tellem_Bond)
fearless.append_member(Yanna_Seldon)
fearless.append_member(Joie)

print("\n--- Équipage du vaisseau ---")
for member in bayta.get_crew():
    member.introduce_yourself()

# Le mentaliste influence un opérateur
Tellem_Bond.act(Gaal_Dornick)
Yanna_Seldon.act(Hugo_Crast)
Joie.act(Hugo_Crast)
