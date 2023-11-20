nom = "Smartphone"
PU = 229
quantité = "100"
print ("Nom du produit :", nom, "Prix Unitaire :", PU, "Quantité :", quantité)
PU += PU * (10/100)
print ('Veuillez indiquer le nombre de quantité souhaité :')
nbquantité = int(input())
print ('Prix après inflation :', PU)