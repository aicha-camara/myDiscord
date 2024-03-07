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

