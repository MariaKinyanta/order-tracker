import os
import csv

# Données initiales
stock_initial = [
    ["Produit", "Quantité"],
    ["Pomme", "10"],
    ["Banane", "15"],
    ["Orange", "5"],
    ["Poire", "8"],
    ["Raisin", "12"],
    ["Mangue", "2"],
    ["Ananas", "3"],
    ["Fraise", "18"]
]

commandes_header = ["Nom", "Produit", "Date"]

if not os.path.exists("stock.csv"):
    with open("stock.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(stock_initial)
    print("✅ stock.csv créé avec succès.")
else:
    print("✔️ stock.csv existe déjà.")

if not os.path.exists("commandes.csv"):
    with open("commandes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(commandes_header)
    print("✅ commandes.csv créé avec succès.")
else:
    print("✔️ commandes.csv existe déjà.")
