import os

dossier = "mission_data"

#Verification de l'existence
if not os.path.exists(dossier):
    print(" Le dossier mission_data n'existe pas")
    exit()

print("mission_data/")

#Lister fichiers
for element in os.listdir(dossier):

    chemin = os.path.join(dossier, element)

    if os.path.isfile(chemin):
        taille = os.path.getsize(chemin) / 1024
        print(f"    {element} ({taille:.1f} Ko)")

#Creer des sous dossiers
rapports = os.path.join(dossier, "rapports")
archives = os.path.join(dossier, "archives")

os.makedirs(rapports, exist_ok=True)
os.makedirs(archives, exist_ok=True)

print("    rapports/")
print("    archives/")