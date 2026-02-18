chemin_journal = "mission_data/journal_bord.txt"
chemin_alertes = "mission_data/alertes.txt"

# Lire le fichier journal
with open(chemin_journal, "r",) as fichier:
    lignes = fichier.readlines()

# nbre total de lignes
nombre_lignes = len(lignes)

print(f"Journal de bord : {nombre_lignes} entrees")

# Pour trouver les alertes
alertes = []

for ligne in lignes:
    if "alerte" in ligne.lower():
        alertes.append(ligne)

print(f"Alertes trouvees ({len(alertes)})")

for alerte in alertes:
    print(alerte.strip())

# Écrire dans alertes.txt
with open(chemin_alertes, "w",) as fichier:
    fichier.writelines(alertes)