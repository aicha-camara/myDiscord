import tkinter as tk
from PIL import ImageTk, Image
import os
from database import Utilisateur

def afficher_channels():
    identification = Utilisateur(host="localhost", user="root", password="e~KPh75=6p[G", database="myDiscord")
    liste_channels = identification.liste_channel()
    identification.fermer_connexion()

    for channel in liste_channels:    
        print(f"Vous avez accès au channel : {channel[0]}")

def main():
    app = tk.Tk()
    app.geometry("1200x640")
    app.title('discord')
    MAIN_COLOR = "#282b30"

    app.tk_setPalette(background="#282b30", foreground="white")
    app.option_add("*Font", ("Century Gothic", 12))

# Obtenez le chemin absolu du fichier image
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_directory, "pattern.png")
