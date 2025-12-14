## Gestion de flotte spatiale (Python)

Ce projet est une application console permettant de gérer une flotte de vaisseaux spatiaux, leurs équipes (operators) et des mentalistes capables d'influencer des membres d'équipage.  
Il inclut un menu interactif, ainsi que des fonctions de sauvegarde et chargement au format JSON.

## Fonctionnalités principales

- Création et gestion de vaisseaux (`Spaceship`) avec type et état (Opérationnel / Endommagé).
- Ajout / suppression de membres d'équipage (`Operator`) dans un vaisseau.
- Affichage des informations d’un équipage.
  -Mentalistes (`Mentalist`) pouvant effectuer une action d’influence sur un operator.
- Vérification de préparation d’un vaisseau (méthode `check_preparation()`).
- Sauvegarde de la flotte en JSON (`save_data`).
- Chargement d’une flotte depuis un JSON (`load_data`).
- Renommage de la flotte.

## Objectifs

- Modéliser les entités principales avec des classes Python :
- `Member`, `Operator`, `Mentalist`, `Spaceship`, `Fleet`
- Gérer les équipages et vaisseaux via un menu interactif.
- Sauvegarder et charger l’état de la flotte dans un fichier JSON.

## Architecture (modules & classes)

Fichiers/modules utilisés :

- `Member.py` : classe(s) de base pour les membres.
- `Operator.py` : classe `Operator` (rôle, expérience, méthodes `introduce_yourself()`, `act()`).
- `Mentalist.py` : classe `Mentalist` (avec `MAX_MANA`, `get_mana()`, `recharge_mana()`, `act(target)`).
- `Spaceship.py` : classe `Spaceship` (nom, type, état, équipage, méthodes `append_member()`, `remove_member()`, `display_crew()`, `check_preparation()`, etc.).
- `Fleet.py` : classe `Fleet` (nom + liste de `Spaceship`, méthodes `append_ship()`, `get_name()`, `set_name()`, etc.).
- `save_load_json.py` : fonctions `save_data(fleet, file_path)` et `load_data(file_path)` + utilitaires éventuels (`choose_ship(fleet)`).

### Bonus : Mode “Mission Galactique”

Cette fonctionnalité supplémentaire a été ajoutée pour rendre le projet plus ludique :  
Lancer une mission galactique pour un vaisseau (option 10 du menu).

#### Conditions pour lancer une mission :

- Le vaisseau doit avoir au moins 1 pilote.
- Le vaisseau doit avoir au moins 1 technicien.
- Le vaisseau doit avoir au moins 1 mentaliste avec un mana ≥ 50.

#### Déroulement :

- L’utilisateur sélectionne un vaisseau depuis la flotte.
- Si les conditions sont remplies :
  - La mission réussit.
  - Tous les opérateurs du vaisseau gagnent +1 point d’expérience.
  - Le mentaliste participant consomme 50 points de mana.
  - Le vaisseau est marqué comme Opérationnel.
- Si les conditions ne sont pas remplies :
  - La mission échoue.
  - Le vaisseau est marqué comme Endommagé.

## Lancement

### Prérequis

- Python 3.10+ recommandé
- Aucune dépendance externe (standard library)

### Exécution

python main.py
