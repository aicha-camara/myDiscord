import tkinter
import customtkinter
import subprocess
from database import Identification
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry("1200x640")
app.title('inscrire')


def button_function():
    # Récupérer les informations saisies par l'utilisateur
    nom_entre = entry1.get()
    prenom_entre = entry2.get()
    email_entre = entry3.get()
    pseudo_entre = entry4.get()
    mot_de_passe_entre = entry5.get()

    # Vérifier que tous les champs sont remplis
    if not nom_entre or not prenom_entre or not email_entre or not pseudo_entre or not mot_de_passe_entre:
        text4 = customtkinter.CTkLabel(master=frame, text="Veuillez remplir tous les champs.", font=('Century Gothic', 12))
        text4.place(x=75, y=320)
        return


    # Insérer l'utilisateur dans la base de données
    identification = Identification(host="localhost", user="root", password="za9?-U5zwD4-6#L", database="myDiscord")
    identification.creer_user(pseudo_entre, mot_de_passe_entre, email_entre, nom_entre, prenom_entre)
    identification.fermer_connexion()

    # Détruire la fenêtre d'inscription
    app.destroy()

    # Rediriger l'utilisateur vers la page de connexion
    subprocess.Popen(["python", "page_connexion.py"])

img1 = ImageTk.PhotoImage(Image.open("assets/pattern.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="S'incrire", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nom')
entry1.place(x=50, y=90)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Prenom')
entry2.place(x=50, y=125)

entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='email')
entry3.place(x=50, y=160)

entry4 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Pseudo')
entry4.place(x=50, y=195)

entry5 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry5.place(x=50, y=230)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Valider", command=button_function, corner_radius=6)
button1.place(x=50, y=280)

app.mainloop()
