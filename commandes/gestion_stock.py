import csv
import os

STOCK_FILE = 'stock.csv'

def charger_stock():
   
    stock = {}
    if not os.path.exists(STOCK_FILE):
        return stock

    with open(STOCK_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 2 or row[0] == "Produit":
                continue
            produit, quantite = row
            stock[produit] = int(quantite)
    return stock

def sauvegarder_stock(stock):
  
    with open(STOCK_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Produit", "Quantité"])
        for produit, quantite in stock.items():
            writer.writerow([produit, quantite])

def verifier_et_reduire_stock(produit):
 
    stock = charger_stock()

    if stock.get(produit, 0) <= 0:
        print(f"❌ Stock insuffisant pour le produit : {produit}")
        return False

    stock[produit] -= 1
    sauvegarder_stock(stock)
    return True
def lire_stock():
    """
    Lit le stock actuel depuis le fichier CSV.
    Renvoie un dictionnaire {produit: quantité}.
    """
    stock = {}
    if not os.path.exists(STOCK_FILE):
        return stock

    with open(STOCK_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            produit = row['Produit']
            quantite = int(row['Quantité'])
            stock[produit] = quantite
    return stock


def afficher_stock():

    stock = lire_stock()
    if not stock:
        print("⚠️  Aucun stock trouvé.")
        return

    print("\n📦 Stock disponible :")
    print(f"{'Produit':<20} | Quantité")
    print("-" * 35)
    for produit, quantite in stock.items():
        print(f"{produit:<20} | {quantite}")
    print()

def produit_existe(produit):
    stock = charger_stock()
    return produit in stock
