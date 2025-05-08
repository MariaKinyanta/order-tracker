
**Order Tracker** est une application en ligne de commande en Python pour gérer un stock de produits et les commandes des clients, avec authentification et deux rôles (client / admin).

---

## 🚀 Fonctionnalités

### Version 1.0  
- Gestion basique du stock (`stock.csv`)  
- Passation et liste des commandes (`commandes.csv`)  
- Suppression et modification de commandes par ID  

### Version 2.0  
- **Authentification & rôles**  
  - Inscription et connexion pour les clients  
  - Compte admin par défaut (login: `admin`, mdp: `admin123`)  
- **Clients**  
  - Passer, lister, modifier et annuler ses propres commandes  
  - Consultation du stock en lecture seule  
- **Administrateurs**  
  - Gestion complète du stock (ajout, suppression de produits)  
  - Annulation des commandes de n’importe quel client (avec notification)  
  - Création et suppression de comptes utilisateurs (avec notification)  
- **Notifications**  
  - Tous les changements critiques (commande, stock, compte) génèrent une notification (simulée par message console).



---

## 📦 Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/MariaKinyanta/order-tracker.git
   cd order-tracker
````

2. (Optionnel) Crée un environnement virtuel :

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Installe les dépendances (aucune bibliothèque externe nécessaire, tout est en standard lib).

---

## ⚙️ Initialisation

Au premier lancement, le script crée automatiquement :

* `stock.csv` avec un stock initial (via `init_csv.py`).
* `commandes.csv` vide.
* `users.csv` avec un compte admin par défaut (`admin` / `admin123`).

Lance simplement :

```bash
python main.py
```

---

## 🛠️ Utilisation

### Menu principal

```
=== Order Tracker ===
1. Connexion
2. Inscription (client)
0. Quitter
```

### Espace Client

```
1. Voir le stock
2. Passer une commande
3. Voir / gérer mes commandes
4. Déconnexion
```

* **Voir / gérer mes commandes** permet de lister, modifier ou annuler (avec confirmation) ses propres commandes.

### Espace Admin

```
1. Voir le stock
2. Ajouter un produit
3. Supprimer un produit
4. Voir toutes les commandes
5. Annuler une commande
6. Gérer les utilisateurs
7. Déconnexion
```

* Toute action critique envoie une notification à l’utilisateur concerné (message console).

---

## 📂 Structure du projet

```
order-tracker/
├── main.py
├── init_csv.py          
├── stock.csv
├── commandes.csv
├── users.csv
└── commandes/
    ├── __init__.py
    ├── auth.py
    ├── gestion_stock.py
    └── gestion_commandes.py
```

---

## 📄 Historique des versions

* **v2.0** – Authentification, gestion des rôles client/admin, notifications.
* **v1.0** – Gestion basique du stock et des commandes.

---



## 🔒 Licence

MIT © 2025 Maria Kinyanta

```
```
