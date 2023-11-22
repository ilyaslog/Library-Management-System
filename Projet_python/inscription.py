import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="python")

cursor = conn.cursor()

def inscription_etudiant(nom, prenom, email, username, mdp):
    try:
        cursor.execute('''
                INSERT INTO utilisateur (nom, prenom, mail, username, mdp)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nom, prenom, email, username, mdp))
        conn.commit()

    except mysql.connector.errors as err:
            # En cas d'erreur, annuler la transaction
            conn.rollback()
            print(f"Erreur lors de l'inscription : {err}")
    finally:
            # Fermer le curseur et la connexion
            cursor.close()
            conn.close()