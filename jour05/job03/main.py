hauteur = int(input("Entrez la hauteur du triangle : "))

for i in range(hauteur):
    espaces_gauche = hauteur - i - 1

    print(" " * espaces_gauche, end="")

    print("/", end="")

    espaces_centre = i * 2
    print(" " * espaces_centre, end="")

    print("\\", end="")

    print()

print("_" * (hauteur * 2))
