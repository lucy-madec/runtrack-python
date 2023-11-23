L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def somme_paires(liste):
    somme = 0

    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre

    return somme

resultat = somme_paires(L)

print("La somme des valeurs paires dans la liste est :", resultat)