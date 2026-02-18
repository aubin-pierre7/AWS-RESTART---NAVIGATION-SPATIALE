import json

def charger_json_securise(chemin):
    try:
        with open(chemin, "r") as f:
            contenu = f.read()

            if contenu.strip() == "":
                print(" Fichier vide")
                return None

            data = json.loads(contenu)

            print(" JSON charge avec succes")
            return data
        
    except FileNotFoundError:
        print(f" Fichier introuvable : {chemin}")

    except json.JSONDecodeError as e:
        print(f"JSON invalide : {e}")

    return None

#Les tests
charger_json_securise("mission_data/missions.json")
charger_json_securise("mission_data/fantome.json")