import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="python")
cursor = conn.cursor()

def insertion_livre(titre, auteur, editeur, ISBN, AnneePublication, NbrExemple):
    try:
        cursor.execute('''
            INSERT INTO livre (titre, auteur, editeur, ISBN, AnneePublication, NbrExemplaire)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (titre, auteur, editeur, ISBN, AnneePublication, NbrExemple))
        conn.commit()
        print("Livre inséré avec succès!")

    except mysql.connector.IntegrityError as err:
        # Handle specific integrity violation errors
        conn.rollback()
        print(f"Erreur d'intégrité lors de l'insertion du livre : {err}")
    except mysql.connector.Error as err:
        # Catch more generic MySQL errors
        conn.rollback()
        print(f"Erreur lors de l'insertion du livre : {err}")

def modifier_livre(idLivre, titre, auteur, editeur, ISBN, AnneePublication, NbrExemple):
    try:
        cursor.execute('''
            UPDATE livre
            SET titre = %s, auteur = %s, editeur = %s, ISBN = %s, AnneePublication = %s, NbrExemplaire = %s
            WHERE id = %s
        ''', (titre, auteur, editeur, ISBN, AnneePublication, NbrExemple, idLivre))
        conn.commit()
        print("Livre modifié avec succès!")

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Erreur lors de la modification du livre : {err}")

def supprimer_livre(idLivre):
    try:
        cursor.execute('''
            DELETE FROM livre
            WHERE id = %s
        ''', (idLivre,))
        conn.commit()
        print("Livre supprimé avec succès!")

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Erreur lors de la suppression du livre : {err}")

def afficher_livres():
    try:
        cursor.execute('''
            SELECT * FROM livre
        ''')
        books = cursor.fetchall()

        if not books:
            print("Aucun livre trouvé.")
        else:
            print("Liste de tous les livres:")
            for book in books:
                print(f"ID: {book[0]}, Titre: {book[1]}, Auteur: {book[2]}, Editeur: {book[3]}, ISBN: {book[4]}, Année de publication: {book[5]}, Nombre d'exemplaires: {book[6]}")

    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération des livres : {err}")

# Close cursor and connection outside functions
cursor.close()
conn.close()
