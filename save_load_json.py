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


def load_data(file_name: str) -> Fleet:
    """
    1) json.load(file) -> dict
    2) créer Spaceship et fleet.append_spaceship(...)
    3) créer Operator/Mentalist et spaceship.append_member(...)
    4) retourner Fleet
    """
    # Étape 1
    path = Path(file_name)
    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {file_name}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Étape 2 : Fleet + Spaceships
    fleet = Fleet()
    fleet_name = data.get("_Fleet__name", "")
    try:
        setattr(
            fleet, "_Fleet__name", fleet_name
        )  # si ta classe a un setter, tu peux l'utiliser à la place
    except Exception:
        pass

    for sd in data.get("_Fleet__spaceships", []):
        name = sd.get("_Spaceship__name", "Unnamed")
        ship_type = sd.get("_Spaceship__shipType", "")
        condition = sd.get("_Spaceship__condition", "")

        # Créer le Spaceship (au minimum avec le nom)
        try:
            spaceship = Spaceship(name)
        except TypeError:
            spaceship = Spaceship(name=name)

        # On remet les attributs privés si nécessaire
        for attr, val in (
            ("_Spaceship__shipType", ship_type),
            ("_Spaceship__condition", condition),
        ):
            try:
                setattr(spaceship, attr, val)
            except Exception:
                pass

        # Intégrer dans la flotte (exigence de la slide)
        fleet.append_spaceship(spaceship)

        # Étape 3 : membres
        for md in sd.get("_Spaceship__crew", []):
            kind = md.get("_Member__kind", "")
            first_name = md.get("_Member__first_name", "")
            last_name = md.get("_Member__last_name", "")
            age = md.get("_Member__age", 0)
            gender = md.get("_Member__gender", "")

            if kind == "Operator":
                role = md.get("_Operator__role", "")
                experience = md.get("_Operator__experience", 0)
                # Essaie avec un constructeur riche, sinon fallback + setattr
                try:
                    member = Operator(
                        first_name, last_name, age, gender, role, experience
                    )
                except TypeError:
                    member = Operator(first_name or last_name or "Unknown")
                    for attr, val in (
                        ("_Member__first_name", first_name),
                        ("_Member__last_name", last_name),
                        ("_Member__age", age),
                        ("_Member__gender", gender),
                        ("_Operator__role", role),
                        ("_Operator__experience", experience),
                    ):
                        try:
                            setattr(member, attr, val)
                        except Exception:
                            pass

            elif kind == "Mentalist":
                mana = md.get("_Mentalist__mana", 0)
                try:
                    member = Mentalist(first_name, last_name, age, gender, mana)
                except TypeError:
                    member = Mentalist(first_name or last_name or "Unknown")
                    for attr, val in (
                        ("_Member__first_name", first_name),
                        ("_Member__last_name", last_name),
                        ("_Member__age", age),
                        ("_Member__gender", gender),
                        ("_Mentalist__mana", mana),
                    ):
                        try:
                            setattr(member, attr, val)
                        except Exception:
                            pass
            else:
                # Type inconnu -> on ignore
                continue

            # Intégrer dans le vaisseau (exigence de la slide)
            spaceship.append_member(member)

    # Étape 4
    return fleet
