from commandes.gestion_stock import afficher_stock  # Ajoute cette ligne

def main():
    print("=== Order Tracker ===")
    print("1. Ajouter une commande")
    print("2. Lister les commandes")
    print("3. Afficher le stock disponible")  # Ajoute cette ligne
    choix = input("Choix (1, 2 ou 3) : ").strip()

    if choix == '1':
        nom = input("Nom du client : ").strip()
        produit = input("Produit commandé : ").strip()
        if not nom or not produit:
            print("⚠️  Nom et produit sont obligatoires.")
            return
        ajouter_commande(nom, produit)

    elif choix == '2':
        lister_commandes()

    elif choix == '3':  
        afficher_stock()

    else:
        print("⚠️  Choix invalide. Veuillez saisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()
