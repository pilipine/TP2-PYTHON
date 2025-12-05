# Attribut des membres de l'équipage
class Member:
    def __init__(self, first_name: str, last_name: str, gender: str, age: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    # méthode
    def introduce_yourself(self) -> str:
        article = "un"
        if self.__gender == "femme":
            article = "une"
        return f"Je m'appelle {self.__first_name} {self.__last_name}, je suis {article} { self.__gender} de {self.__age} ans."

    # Getters des attributs des membres de l'équipe
    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_gender(self) -> str:
        return self.__gender

    def get_age(self) -> int:
        return self.__age

    # Setters des attributs des membres de l'équipe
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def set_gender(self, new_set_gender):
        self.__gender = new_set_gender

    def set_age(self, new_set_age):
        self.__age = new_set_age
