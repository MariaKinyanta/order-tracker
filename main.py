# main.py

from commandes.gestion_commandes import ajouter_commande, lister_commandes

def main():
    print("=== Order Tracker ===")
    print("1. Ajouter une commande")
    print("2. Lister les commandes")
    choix = input("Choix (1 ou 2) : ").strip()

    if choix == '1':
        nom = input("Nom du client : ").strip()
        produit = input("Produit commandé : ").strip()
        if not nom or not produit:
            print("⚠️  Nom et produit sont obligatoires.")
            return
        ajouter_commande(nom, produit)

    elif choix == '2':
        lister_commandes()

    else:
        print("⚠️  Choix invalide. Veuillez saisir 1 ou 2.")

if __name__ == "__main__":
    main()
