# Attribut des membres de l'équipage
from Operator import Operator
class Member:

    def __init__(self, first_name, last_name, gender, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = int(age)

    # Méthode
    def introduce_yourself(self):
        g = str(self.__gender)
        article = "un"
        if g == "femme":
            article = "une"

        role_affiche = self.get_role() or "non défini"
        print(
            f"Je m'appelle {self.__first_name} {self.__last_name}, "
            f"je suis {article} {self.__gender} de {self.__age} ans. "
            f"Mon rôle est : {role_affiche} et mon expérience est de :{ self.__exp}."
        )


    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    # Setters
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def set_gender(self, new_set_gender):
        self.__gender = new_set_gender

    def set_age(self, new_set_age):
        self.__age = int(new_set_age)
