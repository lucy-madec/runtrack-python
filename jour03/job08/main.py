def afficher_selection(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Combinaison non prise en charge")

afficher_selection("fruits", "hiver")
afficher_selection("fruits", "ete")
afficher_selection("legume", "hiver")
afficher_selection("legume", "ete")
afficher_selection("fruits", "automne")