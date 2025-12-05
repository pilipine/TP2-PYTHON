# Import de la classe Member depuis son module

from Member import Member


class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience

    def get_role(self) -> str:
        return self.__role

    def get_experience(self) -> int:
        return self.__experience

    def set_role(self, new_role: str) -> None:
        self.__role = new_role

    def set_experience(self, new_experience: int) -> None:
        self.__experience = int(new_experience)

    def act(self) -> str:
        actions = {
            "technicien": "effectue une maintenance.",
            "pilote": "prend les commandes.",
            "marchand": "négocie les prix.",
            "armurier": "prépare l'armement.",
            "commandant": "donne ses ordres.",
        }
        action = actions.get(self.__role.lower(), "agit.")
        # utilisation des getters de Member

        message = f"{self.get_first_name()} {self.get_last_name()} {action}"
        print(message)
        return message

    def gain_experience(self) -> None:
        self.__experience = self.__experience + 1
