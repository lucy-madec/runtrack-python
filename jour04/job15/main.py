def arrondir_et_trier(liste):
    def arrondir_nombre(nombre):
        entier = int(nombre)
        decimale = nombre - entier
        if decimale >= 0.5:
            return entier + 1
        else:
            return entier

    liste_arrondie = [arrondir_nombre(nombre) for nombre in liste]

    for i in range(1, len(liste_arrondie)):
        valeur_actuelle = liste_arrondie[i]
        position = i
        while position > 0 and liste_arrondie[position - 1] > valeur_actuelle:
            liste_arrondie[position] = liste_arrondie[position - 1]
            position -= 1
        liste_arrondie[position] = valeur_actuelle

    return liste_arrondie

liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

resultat = arrondir_et_trier(liste_nombres)
print(resultat)
