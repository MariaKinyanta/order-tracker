from commandes.auth import init_users, register, login, notify
from commandes.gestion_stock import afficher_stock, charger_stock
from commandes.gestion_commandes import (
    ajouter_commande,
    lister_commandes,
    annuler_commande_par_id,
    modifier_commande_par_id,
    charger_commandes
)

def client_menu(username):
    while True:
        print(f"\n=== Espace Client : {username} ===")
        print("1. Voir le stock")
        print("2. Passer une commande")
        print("3. Voir m1es commandes")
        print("4. Déconnexion")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            afficher_stock()
        elif choix == "2":
            produit = input("Produit commandé : ").strip()
            ajouter_commande(username, produit)
        elif choix == "3":
            commandes = [c for c in charger_commandes() if c["Nom"]==username]
            if not commandes:
                print("⚠️  Vous n'avez aucune commande.")
                continue
            # affichage
            print("\nVos commandes :")
            for idx, cmd in enumerate(commandes, start=1):
                print(f"{idx}. {cmd['Produit']} ({cmd['Date']})")
            sous = input("Annuler (a) / Modifier (m) / Retour (n) : ").strip().lower()
            if sous == "a":
                cid = int(input("ID à annuler : "))
                # retrouver ID global
                global_cmds = charger_commandes()
                # trouver l’index global de la cid-ième commande du client
                indices = [i for i,c in enumerate(global_cmds) if c["Nom"]==username]
                annuler_commande_par_id(indices[cid-1]+1)
            elif sous == "m":
                cid = int(input("ID à modifier : "))
                indices = [i for i,c in enumerate(charger_commandes()) if c["Nom"]==username]
                act = input("1=changer produit, 2=changer nom : ").strip()
                if act=="1":
                    np = input("Nouveau produit : ").strip()
                    modifier_commande_par_id(indices[cid-1]+1, nouveau_produit=np)
                elif act=="2":
                    nn = input("Nouveau nom (client) : ").strip()
                    # on n’autorise pas changement de nom pour client
                    print("❌ Cette option n'est pas disponible.")
                else:
                    print("❌ Choix invalide.")
            # notifications
        elif choix == "4":
            print("👋 Déconnexion.")
            break
        else:
            print("❌ Choix invalide.")

def admin_menu(username):
    while True:
        print(f"\n=== Espace Admin : {username} ===")
        print("1. Voir le stock")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Voir toutes les commandes")
        print("5. Annuler une commande")
        print("6. Gérer les utilisateurs")
        print("7. Déconnexion")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            afficher_stock()
        elif choix == "2":
            p = input("Nom du produit : ").strip()
            q = input("Quantité : ").strip()
            from commandes.gestion_stock import ajouter_produit
            ajouter_produit(p,q)
            notify(username, f"Produit '{p}' ajouté au stock")
        elif choix == "3":
            p = input("Produit à supprimer : ").strip()
            stock = charger_stock()
            if p in stock:
                del stock[p]
                from commandes.gestion_stock import sauvegarder_stock
                sauvegarder_stock(stock)
                print(f"✅ Produit '{p}' supprimé.")
                notify(username, f"Produit '{p}' supprimé")
            else:
                print("❌ Produit introuvable.")
        elif choix == "4":
            lister_commandes()
        elif choix == "5":
            cid = int(input("ID de la commande à annuler : ").strip())
            annuler_commande_par_id(cid)
            # déterminer le client
            cmd = charger_commandes()[cid-1]
            notify(cmd["Nom"], f"Votre commande ID {cid} a été annulée par l'admin")
        elif choix == "6":
            print("\na) Créer un utilisateur")
            print("b) Supprimer un utilisateur")
            action = input("Choix (a/b) : ").strip().lower()
            from commandes.auth import _load_users
            users = _load_users()
            if action=="a":
                u = input("Username : ").strip()
                p = input("Mot de passe : ").strip()
                r = input("Rôle (client/admin) : ").strip()
                if register(u,p,r):
                    notify(u, "Votre compte a été créé par l'admin")
            elif action=="b":
                u = input("Username à supprimer : ").strip()
                if u in users and u!="admin":
                    # suppression
                    rows = [row for row in users if row!=u]
                    # réécriture...
                    from commandes.auth import init_users
                    init_users()  # recrée le fichier
                    for name,info in users.items():
                        if name!=u:
                            register(name, info["password_hash"], info["role"])
                    print(f"✅ Utilisateur '{u}' supprimé.")
                    notify(u, "Votre compte a été supprimé par l'admin")
                else:
                    print("❌ Impossible de supprimer cet utilisateur.")
        elif choix == "7":
            print("👋 Déconnexion.")
            break
        else:
            print("❌ Choix invalide.")

def main():
    init_users()
    while True:
        print("\n=== Order Tracker ===")
        print("1. Connexion")
        print("2. Inscription (client)")
        print("0. Quitter")
        c = input("Votre choix : ").strip()
        if c=="1":
            u = input("Username : ").strip()
            p = input("Mot de passe : ").strip()
            role = login(u,p)
            if role=="client":
                client_menu(u)
            elif role=="admin":
                admin_menu(u)
            else:
                print("❌ Identifiants invalides.")
        elif c=="2":
            u = input("Username désiré : ").strip()
            p = input("Mot de passe : ").strip()
            if register(u,p,"client"):
                print("✅ Inscription réussie, vous pouvez vous connecter.")
        elif c=="0":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    main()
