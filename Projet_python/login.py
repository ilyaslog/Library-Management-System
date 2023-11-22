import mysql.connector
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="projet_py"
)
mycursor = conn.cursor()


def is_admin(username):
    admin_usernames = [
        "admin",
        "superadmin",
    ]  # Liste des utilisateurs considérés comme administrateurs (par defauts)
    return (
        username in admin_usernames
    )  # est une expression booléenne qui vérifie si le nom d'utilisateur (username)
    # se trouve dans la liste admin_usernames


def login(username, password):
    # Requête SQL pour vérifier les informations d'identification dans la table utilisateur
    sql = "SELECT id, statut FROM utilisateur WHERE username = %s AND mdp = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()

    if user:
        user_id, status = user
        if status == 1:
            return -1  # Compte suspendu, renvoie -1
        # Authentification réussie
        if is_admin(username):
            return 1  # Authentifié en tant qu'administrateur
        else:
            return 0  # Authentifié en tant qu'utilisateur normal


def create_account(username, nom, prenom, mail, mdp):
    # Requête SQL pour vérifier si le nom d'utilisateur existe déjà dans la table utilisateur
    check_existing_user_query = "SELECT username FROM utilisateur WHERE username = %s"
    mycursor.execute(
        check_existing_user_query, (username,)
    )  # contenant la valeur du nom d'utilisateur que nous voulons vérifier
    existing_user = mycursor.fetchone()
    if existing_user:
        return -1  # Le nom d'utilisateur existe déjà, renvoie -1
    else:
        # Requête SQL pour insérer des données dans la table utilisateur
        sql = "INSERT INTO utilisateur (nom, Prenom, mail, username, mdp) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, prenom, mail, username, mdp)
        # Exécuter la requête SQL pour insérer les données
        mycursor.execute(sql, val)
        # Valider la transaction
        conn.commit()
        return 1  # Retourne 1 pour indiquer que l'insertion a réussi
