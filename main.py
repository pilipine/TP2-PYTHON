from Member import *
from Operator import *

# Attribut supplémentaire sera : le rôle et l'expérience
# Méthodes supplémentaires : act(), gain_experience(), getters/setters.

action = {
    "pilote": "piloter le vaisseau",
    "technicien": "réparer le vaisseau en cas d'attaque",
    "marchand": "échanger ou vendre des produits",
    "soldat": "combattre les ennemies en cas d'attaque",
}

chris = Member("Chris", "Chevalier", "homme", 33)
print(chris.introduce_yourself())

philippine = Operator("Philippine", "Pelletrat", "femme", 18, "pilote")
print(philippine.introduce_yourself())

philippine.set_role("technicienne")
print(philippine.get_role())
