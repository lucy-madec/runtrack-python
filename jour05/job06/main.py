print("Nombres de marches du phare :")
nb_marches = int(input())

print("Hauteur des marches du phare :")
height = float(input())

def distance(nb_marches, height):
    parcours = (height / 100 * nb_marches) * 5 * 7 * 2
    print(f"Pour {nb_marches} marches de {height} cm, le gardien fait un trajet de {parcours:.2f} mètres par semaine.")

distance(nb_marches, height)