from commandes.gestion_stock import afficher_stock
from commandes.gestion_commandes import ajouter_commande, lister_commandes, annuler_commande

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Voir le stock")
        print("2. Passer une commande")
        print("3. Voir les commandes")
        print("0. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            afficher_stock()

        elif choix == "2":
            nom = input("Nom du client : ").strip()
            produit = input("Nom du produit : ").strip()
            ajouter_commande(nom, produit)

        elif choix == "3":
            while True:
                print("\n📋 Liste des commandes :")
                lister_commandes()
                
                sous_choix = input("\nSouhaitez-vous annuler une commande ? (o pour oui, n pour non) : ").strip().lower()
                if sous_choix == "n":
                    break
                elif sous_choix == "o":
                    nom = input("Nom du client : ").strip()
                    produit = input("Produit à annuler : ").strip()
                    
                    confirmation = input(f"⚠️ Confirmez-vous l'annulation de la commande de '{produit}' pour '{nom}' ? (o/n) : ").strip().lower()
                    if confirmation == "o":
                        annuler_commande(nom, produit)
                    else:
                        print("❌ Annulation annulée par l'utilisateur.")
                else:
                    print("❌ Choix invalide. Répondez par 'o' ou 'n'.")

        elif choix == "0":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
