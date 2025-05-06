# main.py

from commandes.gestion_commandes import ajouter_commande

def main():
    print("=== Order Tracker : Création de commande ===")
    nom = input("Nom du client : ").strip()
    produit = input("Produit commandé : ").strip()

    if not nom or not produit:
        print("⚠️  Nom et produit sont obligatoires.")
        return

    ajouter_commande(nom, produit)

if __name__ == "__main__":
    main()
