import tkinter
import customtkinter
import subprocess
from database import Identification
from PIL import ImageTk,Image


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()
app.geometry("1200x640")
app.title('Login')

def login():
    pseudo_entre = entry1.get()
    mot_de_passe_entre = entry2.get()

    identification = Utilisateur(host="localhost", user="root", password="e~KPh75=6p[G", database="myDiscord")
    liste_utilisateurs = identification.liste_user()
    identification.fermer_connexion()

    pseudo_mot_de_passe_valides = False
    for utilisateur in liste_utilisateurs:
        if utilisateur[5] == pseudo_entre and utilisateur[4] == mot_de_passe_entre:
            pseudo_mot_de_passe_valides = True
            break

