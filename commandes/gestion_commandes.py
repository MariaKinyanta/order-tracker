# commandes/gestion_commandes.py

import csv
import os

# Nom du fichier CSV
CSV_FILE = 'commandes.csv'

def ajouter_commande(nom: str, produit: str) -> None:
    """
    Ajoute une ligne (Nom, Produit) dans le fichier commandes.csv.
    Crée l’en-tête si le fichier n’existait pas.
    """
    # Vérifier si le fichier existe déjà
    nouveau_fichier = not os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if nouveau_fichier:
            writer.writerow(['Nom client', 'Produit commandé'])
        writer.writerow([nom, produit])

    print(f"✅ Commande de « {produit} » pour « {nom} » enregistrée.")
