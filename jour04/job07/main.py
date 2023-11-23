L = [8, 24, 48, 2, 16]

def multiples_de_3(liste):
    compteur = 0

    for nombre in liste:
        if nombre % 3 == 0:
            compteur += 1

    return compteur

resultat = multiples_de_3(L)

print("Le nombre de multiples de 3 dans la liste est :", resultat)
