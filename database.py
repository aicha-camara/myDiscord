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

    def creer_user(self, pseudo, mdp, email, prenom, nom):
        requete = "INSERT INTO utilisateur (pseudo, mdp, email, prenom, nom ) VALUES (%s, %s, %s, %s, %s)"
        valeurs = (pseudo, mdp, email, prenom, nom)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def liste_user(self):
        requete = "SELECT * FROM utilisateur"
        self.curseur.execute(requete)
        resultat = self.curseur.fetchall()
        return resultat

    def mettre_a_jour_mdp(self, user_id, nouveau_mdp):
        requete = "UPDATE utilisateur SET mdp = %s WHERE id = %s"
        valeurs = (nouveau_mdp, user_id)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def supprimer_user(self, user_id):
        requete = "DELETE FROM utilisateur WHERE id = %s"
        valeurs = user_id
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def creer_channel(self, nom_channel, description, role_access):
        requete = "INSERT INTO channel (nom_channel, description, role_access) VALUES (%s, %s, %s)"
        valeurs = (nom_channel, description, role_access)
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def supprimer_channel(self, channel_id):
        requete = "DELETE FROM channel WHERE channel_id = %s"
        valeurs = channel_id
        self.curseur.execute(requete, valeurs)
        self.connexion.commit()

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()
