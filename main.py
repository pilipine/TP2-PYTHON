from Member import *
from Operator import *
from Mentalist import Mentalist, MAX_MANA


# Instancier un nouveau membre d'équipage
Bel_riose = Operator("Bel", "Riose", "Homme", 48, "commandant")
Bel_riose.introduce_yourself()
Bel_riose.act()

Gaal_Dornick = Operator("Gaal", "Dornick", "Femme", 34, "technicien")
Gaal_Dornick.introduce_yourself()
Gaal_Dornick.act()

Salvor_Hardin = Operator("Salvor", "Hardin", "Femme", 28, "Armurier")
Salvor_Hardin.introduce_yourself()
Salvor_Hardin.act()

Hugo_Crast = Operator("Hugo", "Crast", "Homme", 37, "Pilote")
Hugo_Crast.introduce_yourself()
Hugo_Crast.act()


# Instancier des mentalistes   tellem Bond H 48 100MANA, Yanna Seldon F 52 100MANA, JOIE F 25 100  MANA

Tellem_Bond= Mentalist("Tellem","Bond","Homme",48,MAX_MANA)
print(f"Mana de départ est de :{Tellem_Bond.get_mana()}")
Tellem_Bond.recharge_mana()
print(f" Après recharge, votre mana est de :{Tellem_Bond.get_mana}")

Yanna_Seldon= Mentalist("Yanna","Seldon","Femme",52,MAX_MANA)
print(f"Mana de départ est de :{Yanna_Seldon.get_mana()}")
Yanna_Seldon.recharge_mana()
print(f" Après recharge, votre mana est de :{Yanna_Seldon.get_mana}")

Joie= Mentalist("joie","","Femme",25,MAX_MANA)
print(f"Mana de départ est de :{Joie.get_mana()}")
Joie.recharge_mana()
print(f" Après recharge, votre mana est de :{Joie.get_mana}")


# Le mentaliste influence un opérateur
Tellem_Bond.act(Gaal_Dornick) 
Yanna_Seldon.act(Hugo_Crast) 
Joie.act(Hugo_Crast) 
