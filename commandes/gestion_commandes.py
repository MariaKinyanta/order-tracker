import csv
import os
from datetime import datetime
from .gestion_stock import verifier_et_reduire_stock, lire_stock, normaliser_nom_produit


COMMANDES_FILE = 'commandes.csv'


def ajouter_commande(nom, produit):
    nom_produit_normalise = normaliser_nom_produit(produit)

    if not nom_produit_normalise:
        print(f"❌ Le produit '{produit}' n'existe pas dans le stock.")
        return

    if not verifier_et_reduire_stock(nom_produit_normalise):
        return

    fichier_existe = os.path.exists(COMMANDES_FILE)
    with open(COMMANDES_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not fichier_existe:
            writer.writerow(["Nom", "Produit", "Date"])
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([nom, nom_produit_normalise, date])

    stock = lire_stock()
    quantite_restante = stock.get(nom_produit_normalise, 0)
    print(f"✅ Commande ajoutée. Il reste {quantite_restante} unité(s) de '{nom_produit_normalise}' en stock.")


def lister_commandes() -> None:
    if not os.path.exists(COMMANDES_FILE):
        print("⚠️  Aucune commande trouvée (fichier inexistant).")
        return

    with open(COMMANDES_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        lignes = list(reader)

    if len(lignes) <= 1:
        print("⚠️  Le fichier ne contient pas de commande.")
        return

    entete, *data = lignes
    print(f"\n{entete[0]:<20} | {entete[1]:<20} | {entete[2]}")
    print("-" * 70)
    for nom, produit, date in data:
        print(f"{nom:<20} | {produit:<20} | {date}")
    print(f"\n📋 {len(data)} commande(s) trouvée(s).")
