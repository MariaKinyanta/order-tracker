import csv
import os
from .gestion_stock import verifier_et_reduire_stock 

CSV_FILE = 'commandes.csv'


from commandes.gestion_stock import verifier_et_reduire_stock

def ajouter_commande(nom, produit):
   
    if not verifier_et_reduire_stock(produit):
        return  # 

    fichier_existe = os.path.exists(COMMANDES_FILE)
    with open(COMMANDES_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not fichier_existe:
            writer.writerow(["Nom", "Produit", "Date"])
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([nom, produit, date])
    print("✅ Commande ajoutée.")


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
