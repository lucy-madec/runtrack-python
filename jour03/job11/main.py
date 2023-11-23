def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60

    if heures == 0:
        temps_texte = f"{minutes_restantes} minutes"
    elif heures == 1:
        temps_texte = f"{heures} heure et {minutes_restantes} minutes"
    else:
        temps_texte = f"{heures} heures et {minutes_restantes} minutes"

    print(temps_texte)

time_to_text(75)
time_to_text(120)
time_to_text(45)
