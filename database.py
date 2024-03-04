import mysql.connector

class Utilisateur:

    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="e~KPh75=6p[G",
            database="myDiscord"
        )
        self.curseur = self.connexion.cursor()

    def creer_user(self, pseudo, mots_de_passe, email, prenom, nom):
        requete = "INSERT INTO identifiant (pseudo, mots_de_passe, email, prenom, nom ) VALUES (%s, %s, %s, %s, %s )"
        valeurs = (pseudo, mots_de_passe, email, prenom, nom)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def liste_user(self):
        requete = "SELECT * FROM identifiant"
        self.curseur.execute(requete)
        resultat = self.curseur.fetchall()
        return resultat

    def mettre_a_jour_mdp(self, user_id, nouveau_mots_de_passe):
        requete = "UPDATE identifiant SET mots_de_passe = %s WHERE id = %s"
        valeurs = (nouveau_mots_de_passe, user_id)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def supprimer_user(self, user_id):
        requete = "DELETE FROM identifiant WHERE id = %s"
        valeurs = (user_id,)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()
