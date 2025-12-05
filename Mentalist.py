
# Import de la classe Member depuis son module
from Member import Member
from Operator import Operateur  


class Mentalist(Member):

    """
    Mentalist hérite de Member et ajoute :
      - mana (int) : points de mana (initialisé à 100)

    Méthodes :
      - act(operator): réduit le mana de 20 et force l'opérateur ciblé à agir (operator.act())
      - recharge_mana(): augmente le mana de 50 (sans dépasser 100)
      - Getters/Setters pour mana
    """

    def __init__(self, first_name: str, last_name: str, gender: str, age: int, mana: int = 100):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = int(mana)

    # --------- Getter/Setter mana ----------
    def get_mana(self) -> int:
        return self.__mana

    def set_mana(self, new_mana: int) -> None:
        self.__mana = max(0, int(new_mana))  # on évite les valeurs négatives

    # --------- Méthodes du TP ----------
    def act(self, operator) -> str:
        """
        Influence un opérateur : dépense 20 mana et appelle operator.act().

        - Si le mana < 20 : affiche un message d'insuffisance et n'agit pas.
        - 'operator' doit être un objet (Operator ou du moins posséder une méthode act()).
        """
        # Vérification du mana
        if self.__mana < 20:
            msg = f"{self.first_name} {self.last_name} n'a pas assez de mana pour influencer l'opérateur."
            print(msg)
            return msg

        # Vérification basique du paramètre operator
        if operator is None or not hasattr(operator, "act"):
            msg = "Cible invalide : 'operator' doit être un objet avec une méthode act()."
            print(msg)
            return msg

        # Dépense du mana
        self.__mana -= 20

        # Message d'influence
        msg = f"{self.first_name} {self.last_name} utilise ses capacités mentales (mana -20)."
        print(msg)

        # Forcer l'opérateur à agir
        result = operator.act()  # operator.act() doit retourner/afficher une action

        return msg + " " + str(result)

    def recharge_mana(self) -> int:
        """
        Recharge de 50 points de mana, sans dépasser 100.
        Retourne le nouveau niveau de mana.
        """
        self.__mana = min(100, self.__mana + 50)
        print(f"Mana de {self.first_name} {self.last_name} rechargé à {self.__mana}.")
