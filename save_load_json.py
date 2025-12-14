# save_load_json.py
import json  # Étape 1 et 3
import ast  # Étape 2
from pathlib import Path


# === Helpers internes pour fabriquer un dict au bon format JSON (name-manglé) ===
def _pick(obj, *names, default=None):
    for n in names:
        if hasattr(obj, n):
            return getattr(obj, n)
    return default


def _member_to_dict(m):
    kind = m.__class__.__name__  # "Operator" ou "Mentalist"
    d = {
        "_Member__first_name": _pick(
            m, "_Member__first_name", "first_name", default=""
        ),
        "_Member__last_name": _pick(m, "_Member__last_name", "last_name", default=""),
        "_Member__age": _pick(m, "_Member__age", "age", default=0),
        "_Member__gender": _pick(m, "_Member__gender", "gender", default=""),
        "_Member__kind": kind,
    }
    if kind == "Operator":
        d["_Operator__role"] = _pick(m, "_Operator__role", "role", default="")
        d["_Operator__experience"] = _pick(
            m, "_Operator__experience", "experience", default=0
        )
    elif kind == "Mentalist":
        d["_Mentalist__mana"] = _pick(m, "_Mentalist__mana", "mana", default=0)
    return d


def _spaceship_to_dict(s):
    crew_list = []
    for mem in _pick(s, "_Spaceship__crew", "crew", default=[]) or []:
        crew_list.append(_member_to_dict(mem))
    return {
        "_Spaceship__name": _pick(s, "_Spaceship__name", "name", default=""),
        "_Spaceship__shipType": _pick(
            s, "_Spaceship__shipType", "shipType", "type", default=""
        ),
        "_Spaceship__condition": _pick(
            s, "_Spaceship__condition", "condition", default=""
        ),
        "_Spaceship__crew": crew_list,
    }


def _fleet_to_dict(fleet):
    ships = []
    for s in _pick(fleet, "_Fleet__spaceships", "spaceships", default=[]) or []:
        ships.append(_spaceship_to_dict(s))
    return {
        "_Fleet__name": _pick(fleet, "_Fleet__name", "name", default=""),
        "_Fleet__spaceships": ships,
    }


# === 1) Fonction de SAUVEGARDE (3 étapes de la slide) ===
def save_data(fleet, file_name: str) -> None:
    """
    1) json.dumps(...) -> chaîne JSON
    2) ast.literal_eval(...) -> dict Python
    3) json.dump(dict, file) -> fichier JSON
    """
    # Étape 1 : on contrôle la structure pour matcher exactement ton JSON
    serializable = _fleet_to_dict(fleet)
    json_string = json.dumps(serializable, sort_keys=True, indent=4)

    # Étape 2 : conversion chaîne -> dict via ast.literal_eval (exigence de la slide)
    normalized = (
        json_string.replace("true", "True")
        .replace("false", "False")
        .replace("null", "None")
    )
    try:
        json_dict = ast.literal_eval(normalized)
    except (SyntaxError, ValueError) as e:
        raise ValueError(f"ast.literal_eval a échoué : {e}")

    # Étape 3 : écriture dans le fichier
    path = Path(file_name)
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(json_dict, f, ensure_ascii=False, indent=4)


# === 2) Fonction de CHARGEMENT (4 étapes de la slide) ===
# On reconstruit Fleet -> Spaceship -> Members en appelant les méthodes demandées.
# ⚠️ Adapte les imports selon TON projet.
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet



# save_load_json.py
import json
from pathlib import Path

from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist

def load_data(file_name: str) -> Fleet:
    """
    1) json.load(file) -> dict
    2) créer Spaceship et fleet.append_ship(...)
    3) créer Operator/Mentalist et spaceship.append_member(...)
    4) retourner Fleet
    """
    # Étape 1 : charger
    path = Path(file_name)
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_name}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Étape 2 : Fleet avec SON NOM (ta classe Fleet exige 'name')
    fleet_name = data.get("_Fleet__name", "Flotte")
    fleet = Fleet(fleet_name)

    # Vaisseaux
    for sd in data.get("_Fleet__spaceships", []):
        name      = sd.get("_Spaceship__name", "SansNom")
        ship_type = sd.get("_Spaceship__shipType", "Marchand")
        condition = sd.get("_Spaceship__condition", "Opérationnel")

        # Signature de ta classe Spaceship : (name, ship_type, crew=None, condition="Opérationnel")
        spaceship = Spaceship(name=name, ship_type=ship_type, condition=condition)

        # Ajout dans la flotte (méthode réelle : append_ship ou add_ship)
        if hasattr(fleet, "append_ship"):
            fleet.append_ship(spaceship)
        else:
            fleet.add_ship(spaceship)

        # Membres
        for md in sd.get("_Spaceship__crew", []):
            kind       = md.get("_Member__kind", "")
            first_name = md.get("_Member__first_name", "")
            last_name  = md.get("_Member__last_name", "")
            gender     = md.get("_Member__gender", "")
            age        = md.get("_Member__age", 0)

            if kind == "Operator":
                role       = md.get("_Operator__role", "")
                experience = md.get("_Operator__experience", 0)
                # ⚠️ ordre requis par ta classe Operator :
                # Operator(first_name, last_name, gender, age, role, experience)
                member = Operator(first_name, last_name, gender, age, role, experience)

            elif kind == "Mentalist":
                mana = md.get("_Mentalist__mana", 0)
                # Hypothèse : Mentalist(first_name, last_name, gender, age, mana)
                member = Mentalist(first_name, last_name, gender, age, mana)

            else:
                # Type inconnu -> ignorer
                continue

            spaceship.append_member(member)

    # Étape 4 : renvoyer la flotte
    return fleet
