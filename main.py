from Member import *
from Operator import *
from Mentalist import *
from Spaceship import *


# main.py

if __name__ == "__main__":
    op1 = Operator("Bel", "Riose", "Homme", 48, "Pilote")
    op1.act()  # -> "Gaal Dornick répare le vaisseau"
    op1.gain_experience()
    print(op1.get_experience())  # -> 1

    op2 = Operator("Salvor", "Hardin", "F", 27, "pilote", experience=2)
    op2.act()  # -> "Salvor Hardin pilote le vaisseau"
    op2.gain_experience(3)
    print(op2.get_experience())  # -> 5

    op3 = Operator("Hober", "Mallow", "M", 30, "marchand")
    op3.act()  # -> "Hober Mallow ne fait rien"
