
# main.py
from Member import Member
from Operator import Operator
from Mentalist import Mentalist, MAX_MANA
from Spaceship import Spaceship

# Instancier de nouveaux membres d'équipage (Operators)
Bel_riose = Operator("Bel", "Riose", "Homme", 48, "commandant",experience=0)
Bel_riose.introduce_yourself()
Bel_riose.act()

Gaal_Dornick = Operator("Gaal", "Dornick", "Femme", 34, "technicien",experience=0)
Gaal_Dornick.introduce_yourself()
Gaal_Dornick.act()

Salvor_Hardin = Operator("Salvor", "Hardin", "Femme", 28, "armurier",experience=0) 
Salvor_Hardin.introduce_yourself()
Salvor_Hardin.act()

Hugo_Crast = Operator("Hugo", "Crast", "Homme", 37, "pilote",experience=0) 
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

# Le mentaliste influence un opérateur
Tellem_Bond.act(Gaal_Dornick)
Yanna_Seldon.act(Hugo_Crast)
Joie.act(Hugo_Crast)


#Créer un vaisseau
ship = Spaceship(name="Bayta", shipType="Marchand",crew= 4 condition="Opérationnel")
ship = Spaceship(name="Dark Nebula", shipType="Guerre",crew="5 dont 1 mentaliste" condition="Endommagé")
ship = Spaceship(name="Fearless", shipType="Guerre",crew= "5 dont 1 mentaliste"  condition="Opérationnel")
ship = Spaceship(name="Unimara", shipType="Marchand",crew= "5 dont 1 mentaliste"  condition="Opérationnel")
ship = Spaceship(name="Weinis", shipType="Marchand",crew= 4 condition="Endommagé")
