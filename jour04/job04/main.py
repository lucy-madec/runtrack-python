def ajout_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    
    fruits.insert(2, "Mangue")
    
    return fruits

resultat = ajout_mangue()
print(resultat)
