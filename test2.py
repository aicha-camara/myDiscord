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

    # Charger l'image
    image = Image.open(image_path)
    img1 = ImageTk.PhotoImage(image)

    # Créer un widget Label pour afficher l'image
    frame = tk.Label(app, image=img1)
    frame.pack()

    # Création boite gauche nom channel
    subframe = tk.Frame(master=app, width=320, height=600, bg=MAIN_COLOR)
    subframe.place(relx=0.3, rely=0.5, anchor=tk.E)

    l5 = tk.Label(master=subframe, text="LaPlateforme", font=('Century Gothic', 20))
    l5.place(x=40, y=45)

    # Création boite droite textuel
    subframe2 = tk.Frame(master=app, width=700, height=600)
    subframe2.place(relx=0.9, rely=0.5, anchor=tk.E)
    app.mainloop()

# Appelez la méthode channel ici si nécessaire

if __name__ == "__main__":
    main()
    afficher_channels()
    # Appelez la méthode channel ici si vous voulez qu'elle s'exécute après la fermeture de la fenêtre
