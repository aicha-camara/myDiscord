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


def button_function():
    # Récupérer le pseudo et le mot de passe saisis par l'utilisateur
    pseudo_entre = entry1.get()
    mot_de_passe_entre = entry2.get()

    # Rechercher dans la base de données si les informations d'identification sont valides
    identification = Identification(host="localhost", user="root", password="za9?-U5zwD4-6#L", database="user")
    liste_utilisateurs = identification.liste_user()
    identification.fermer_connexion()

    pseudo_mot_de_passe_valides = False
    for utilisateur in liste_utilisateurs:
        if utilisateur[1] == pseudo_entre and utilisateur[2] == mot_de_passe_entre:
            pseudo_mot_de_passe_valides = True
            break

    if pseudo_mot_de_passe_valides:
        # Détruire la fenêtre de connexion
        app.destroy()

        # Créer une nouvelle fenêtre de bienvenue
        w = customtkinter.CTk()
        w.geometry("1280x720")
        w.title('Welcome')

        # Ajouter un label à la fenêtre de bienvenue
        l1 = customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Lancer le fichier principal (main.py) dans un nouveau processus
        subprocess.Popen(["python", "main.py"])
    else:
        # Informer l'utilisateur que les informations d'identification sont incorrectes
        print("Pseudo ou mot de passe incorrect.")
        # Vous pouvez également afficher un message d'erreur à l'utilisateur ou réinitialiser les champs de saisie.


img1=ImageTk.PhotoImage(Image.open("assets/pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Pseudo')
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)



# You can easily integrate authentication system 

app.mainloop()
