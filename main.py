from commandes.gestion_stock import afficher_stock
from commandes.gestion_commandes import (
    ajouter_commande,
    lister_commandes,
    annuler_commande_par_id,
    modifier_commande_par_id,
    charger_commandes
)

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
            produit = input("Produit commandé : ").strip()
            ajouter_commande(nom, produit)

        elif choix == "3":
            commandes = charger_commandes()
            if not commandes:
                print("⚠️  Aucune commande enregistrée : Veillez choisir un choix ci-dessous.")
                continue

            while True:
                print("\n📋 Liste des commandes :")
                lister_commandes()

                print("\na) Annuler une commande ")
                print("b) Modifier une commande ")
                print("n) Retour au menu principal")
                cmd = input("Choix (a/b/c) : ").strip().lower()

                if cmd == "c":
                    break

                elif cmd == "a":
                    try:
                        cid = int(input("Entrez l’ID de la commande à annuler : ").strip())
                        annuler_commande_par_id(cid)
                    except ValueError:
                        print("❌ ID invalide. Veuillez entrer un nombre.")

                elif cmd == "b":
                    try:
                        cid = int(input("Entrez l’ID de la commande à modifier : ").strip())
                    except ValueError:
                        print("❌ ID invalide. Veuillez entrer un nombre.")
                        continue

                    print("1) Changer le nom du client")
                    print("2) Changer le produit")
                    act = input("Votre choix (1/2) : ").strip()
                    if act == "1":
                        nn = input("Nouveau nom du client : ").strip()
                        modifier_commande_par_id(cid, nouveau_nom=nn)
                    elif act == "2":
                        np = input("Nouveau produit : ").strip()
                        modifier_commande_par_id(cid, nouveau_produit=np)
                    else:
                        print("❌ Option invalide pour la modification.")

                else:
                    print("❌ Option invalide. Répondez par 'a', 'b' ou 'c'.")

        elif choix == "0":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
