def test(notes):
    nb = []
    dark_vador = []
    for nb in notes:
        if nb < 40:
            dark_vador.append(nb)
        else:
            yoda = ((nb // 5) + 1) * 5
            if yoda - nb < 3:
                dark_vador.append(yoda)
            else:
                dark_vador.append(nb)
    if dark_vador != []:
        print(f"{len(dark_vador)} échecs au test avec {dark_vador}")
    else:
        print("Tu as réussi jeune Padawan")

test([69, 6, 28, 25, 92, 47, 20])