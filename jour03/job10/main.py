def nb_pair_impair(nombre):
    if nombre % 2 == 0 and nombre > 0 and isinstance(nombre, int):
        print("Nombre pair")    
    elif nombre % 2 != 0 and nombre > 0 and isinstance(nombre, int):
        print("Nombre impair")
    else:
        print("Ce nombre n'est pas entier ou positif.")

nb_pair_impair(46)
nb_pair_impair(45)
nb_pair_impair(-13)