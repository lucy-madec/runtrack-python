def my_long_word(n, phrase):
    mots = ""
    mot = ""
    compteur = 0

    for lettre in phrase:
        if ('a' <= lettre <= 'z' or 'A' <= lettre <= 'Z' or '0' <= lettre <= '9' <= '9' or lettre.isalpha()):
            mot += lettre
            compteur += 1
        elif mot:
            if compteur > n:
                mots += mot + " "
            mot = ""
            compteur = 0
    
    if mot and compteur > n:
        mots += mot

    return mots

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(resultat)
