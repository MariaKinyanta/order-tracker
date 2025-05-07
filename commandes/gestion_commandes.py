import csv
import os
from datetime import datetime
from .gestion_stock import verifier_et_reduire_stock, produit_existe
from .gestion_stock import verifier_et_reduire_stock, produit_existe, lire_stock  


COMMANDES_FILE = 'commandes.csv'

def ajouter_commande(nom, produit):
    if not produit_existe(produit):
        print(f"❌ Le produit '{produit}' n'existe pas dans le stock.")
        return

    if not verifier_et_reduire_stock(produit):
        return  

    fichier_existe = os.path.exists(COMMANDES_FILE)
    with open(COMMANDES_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not fichier_existe:
            writer.writerow(["Nom", "Produit", "Date"])
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([nom, produit, date])

    stock = lire_stock()
    quantite_restante = stock.get(produit, 0)
    print(f"✅ Commande ajoutée. Il reste {quantite_restante} unité(s) de '{produit}' en stock.")

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
