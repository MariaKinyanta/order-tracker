import csv
import os
from datetime import datetime
from .gestion_stock import (
    verifier_et_reduire_stock,
    lire_stock,
    normaliser_nom_produit,
    sauvegarder_stock
)

COMMANDES_FILE = 'commandes.csv'

def charger_commandes():
    """Retourne liste de dicts [{'Nom':…, 'Produit':…, 'Date':…}, …]."""
    if not os.path.exists(COMMANDES_FILE):
        return []
    with open(COMMANDES_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def sauvegarder_commandes(commandes):
    """Écrit la liste de commandes (list of dict) dans le CSV."""
    with open(COMMANDES_FILE, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['Nom', 'Produit', 'Date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(commandes)

def ajouter_commande(nom, produit):
    nom_produit = normaliser_nom_produit(produit)
    if not nom_produit:
        print(f"❌ Le produit '{produit}' n'existe pas dans le stock.")
        return

    if not verifier_et_reduire_stock(nom_produit):
        return

    commandes = charger_commandes()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commandes.append({'Nom': nom, 'Produit': nom_produit, 'Date': date})
    sauvegarder_commandes(commandes)

    stock = lire_stock()
    q = stock.get(nom_produit, 0)
    print(f"✅ Commande ajoutée (ID {len(commandes)}). Il reste {q} unité(s) de '{nom_produit}'.")

def lister_commandes():
    commandes = charger_commandes()
    if not commandes:
        print("⚠️  Aucune commande à afficher.")
        return

    print(f"\n{'ID':<4} | {'Nom':<15} | {'Produit':<15} | Date")
    print("-" * 60)
    for idx, cmd in enumerate(commandes, start=1):
        print(f"{idx:<4} | {cmd['Nom']:<15} | {cmd['Produit']:<15} | {cmd['Date']}")
    print(f"\n📋 {len(commandes)} commande(s).")

def annuler_commande_par_id(cmd_id):
    commandes = charger_commandes()
    if not commandes:
        print("⚠️  Aucune commande enregistrée.")
        return
    if cmd_id < 1 or cmd_id > len(commandes):
        print(f"❌ Aucune commande avec l’ID {cmd_id}.")
        return

    cmd = commandes.pop(cmd_id - 1)
    # restaurer le stock
    stock = lire_stock()
    stock[cmd['Produit']] = stock.get(cmd['Produit'], 0) + 1
    sauvegarder_stock(stock)
    sauvegarder_commandes(commandes)
    print(f"✅ Commande ID {cmd_id} annulée et stock de '{cmd['Produit']}' restauré.")

def modifier_commande_par_id(cmd_id, nouveau_nom=None, nouveau_produit=None):
    commandes = charger_commandes()
    if not commandes:
        print("⚠️  Aucune commande enregistrée.")
        return
    if cmd_id < 1 or cmd_id > len(commandes):
        print(f"❌ Aucune commande avec l’ID {cmd_id}.")
        return

    cmd = commandes[cmd_id - 1]
    ancien = (cmd['Nom'], cmd['Produit'])
    # changement de produit
    if nouveau_produit:
        nom_produit = normaliser_nom_produit(nouveau_produit)
        if not nom_produit:
            print(f"❌ Nouveau produit '{nouveau_produit}' introuvable.")
            return
        # remettre ancien produit en stock
        stock = lire_stock()
        stock[ancien[1]] = stock.get(ancien[1], 0) + 1
        sauvegarder_stock(stock)
        # réserver nouveau produit
        if not verifier_et_reduire_stock(nom_produit):
            print("❌ Stock insuffisant pour le nouveau produit.")
            # retenter ancien
            stock = lire_stock()
            stock[ancien[1]] -= 1
            sauvegarder_stock(stock)
            return
        cmd['Produit'] = nom_produit

    # changement de nom
    if nouveau_nom:
        cmd['Nom'] = nouveau_nom

    sauvegarder_commandes(commandes)
    print(f"✅ Commande ID {cmd_id} modifiée : {ancien} → ({cmd['Nom']}, {cmd['Produit']}).")
