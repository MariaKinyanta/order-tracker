import csv
import os
import hashlib

USERS_FILE = "users.csv"

def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def init_users():
    """Crée le fichier users.csv avec un admin par défaut si vide."""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username","password_hash","role"])
            # mot de passe par défaut : admin123
            writer.writerow(["admin", _hash("admin123"), "admin"])
        print("✅ users.csv initialisé avec un admin par défaut (login: admin / mdp: admin123).")

def register(username: str, password: str, role: str="client") -> bool:
    users = _load_users()
    if username in users:
        return False
    with open(USERS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, _hash(password), role])
    print(f"✅ Compte '{username}' créé avec le rôle '{role}'.")
    return True

def login(username: str, password: str):
    """Vérifie les credentials. Retourne role ou None."""
    users = _load_users()
    h = _hash(password)
    if username in users and users[username]["password_hash"] == h:
        return users[username]["role"]
    return None

def _load_users():
    d = {}
    if not os.path.exists(USERS_FILE):
        return d
    with open(USERS_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            d[row["username"]] = {
                "password_hash": row["password_hash"],
                "role": row["role"]
            }
    return d

def notify(username: str, message: str):
    """Simulation de notification (print)."""
    print(f"🔔 Notification pour '{username}': {message}")
