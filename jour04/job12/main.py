ma_liste = [64, 34, 25, 12, 22, 11, 90]
def tri_selection(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n - 1):
        indice_min = i

        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        temp = liste[i]
        liste[i] = liste[indice_min]
        liste[indice_min] = temp

    return liste

resultat = tri_selection(ma_liste)
print("Liste triée:", resultat)
