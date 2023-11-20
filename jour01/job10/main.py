montant_initial = 1000
taux_rendement_annuel = 5
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel initial :", round(gain_annuel), "€")
montant_initial += 5000
taux_rendement_annuel += 2
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Nouveau gain annuel :", round(nouveau_gain_annuel), "€")
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1
montant_final = montant_initial + nouveau_gain_annuel
print("Nouveau gain annuel :", round(nouveau_gain_annuel), "€")
print("Montant final de l'investissement :", round(montant_final), "€")