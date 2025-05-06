# commandes/gestion_commandes.py

import csv
import os

CSV_FILE = 'commandes.csv'

def ajouter_commande(nom: str, produit: str) -> None:
    nouveau_fichier = not os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if nouveau_fichier:
            writer.writerow(['Nom client', 'Produit commandé'])
        writer.writerow([nom, produit])

    print(f"✅ Commande de « {produit} » pour « {nom} » enregistrée.")

def lister_commandes() -> None:
    if not os.path.exists(CSV_FILE):
        print("⚠️  Aucune commande trouvée (fichier inexistant).")
        return

    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        lignes = list(reader)

    if len(lignes) <= 1:
        print("⚠️  Le fichier ne contient pas de commande.")
        return

    entete, *data = lignes
    print(f"\n{entete[0]:<20} | {entete[1]}")
    print("-" * 40)
    for nom, produit in data:
        print(f"{nom:<20} | {produit}")
    print(f"\n📋 {len(data)} commande(s) trouvée(s).")
