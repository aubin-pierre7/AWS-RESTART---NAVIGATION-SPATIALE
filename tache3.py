import json 

chemin = "mission_data/missions.json"  #chemin du fichier

with open(chemin, "r") as f: 
    data = json.load(f)  #convertit le JSON en dictionnaire Python

missions = data["missions"]  

budget_total = 0  

plus_longue = missions[0]  
plus_courte = missions[0]

for mission in missions:  #boucle sur chaque mission

    id = mission["id"]  
    nom = mission["nom"]  
    destination = mission["destination"] 
    duree = mission["duree_jours"]  
    equipage = len(mission["equipage"])  
    budget = mission["budget_millions_usd"]  

    print(f"[{id}] {nom} → {destination} | {duree} jours | Equipage : {equipage} | Budget : {budget:,} M$")

    budget_total += budget  #budget total

    if duree > plus_longue["duree_jours"]:  # comparaison de la duree
        plus_longue = mission  

    if duree < plus_courte["duree_jours"]:
        plus_courte = mission

print(f"\nBudget total : {budget_total:,} M$")
print(f"Mission la plus longue : {plus_longue['nom']}")
print(f"Mission la plus courte : {plus_courte['nom']}")
