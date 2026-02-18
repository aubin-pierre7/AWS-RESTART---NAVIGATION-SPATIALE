import json
import math
def charger_corps_celestes():

    with open("mission_data/corps_celestes.json", "r") as f:

        return json.load(f)["corps_celestes"]

def distance_interplanetaire(c1, c2, corps):

    d1 = None
    d2 = None

    for c in corps:

        if c["nom"] == c1:
            d1 = c["distance_soleil_mkm"]

        if c["nom"] == c2:
            d2 = c["distance_soleil_mkm"]

    return abs(d1 - d2)

def temps_trajet(distance_mkm, vitesse_km_s):

    distance_km = distance_mkm * 1_000_000

    secondes = distance_km / vitesse_km_s

    jours = secondes / 86400

    return jours

def poids_sur_corps(masse, gravite):

    return masse * gravite

# Ajout des tests
if __name__ == "__main__":

    corps = charger_corps_celestes()

    d = distance_interplanetaire("Terre", "Mars", corps)

    print("Distance:", d)

    t = temps_trajet(d, 11)

    print("Temps:", t)

    print("Poids sur Mars:", poids_sur_corps(80, 3.72))