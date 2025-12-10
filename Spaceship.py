
# spaceship.py
# Imports des classes 
from Member import Member
from Operator import Operateur
from Mentalist import Mentalist


class Spaceship:

    def __init__(self, name, shiptype, crew, condition):
        self.__name= name
        self.__shiptype= shiptype
        self.__crew= []
        self.__condition= condition


# --------- Getter/Setter mana ----------
    def get_mana(self) -> int:
        return self.__name
    
    def get_shiptype(self) -> int:
        return self.__shiptype
    
    def get_crew(self) -> int:
        return self.__crew
    
    def get_condition(self):
        return self.__condition
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_shiptype(self, new_shiptype):
        self.__shiptype = new_shiptype
    
    def set_crew(self, new_crew):
        self.__crew = new_crew

    def set_condition(self, new_condition):
        self.__condition = new_condition
    