import os
import shutil
from datetime import datetime

base = "mission_data"

source = os.path.join(base, "journal_bord.txt")
archives = os.path.join(base, "archives")

date = datetime.now().strftime("%Y-%m-%d")

destination = os.path.join(archives, f"journal_bord_{date}.txt")

shutil.copy(source, destination)

print(" Fichier archive :", destination)