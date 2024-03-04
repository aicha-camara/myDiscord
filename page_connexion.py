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
    
    if pseudo_mot_de_passe_valides:
        app.destroy()
        subprocess.Popen(["python", "test.py"])

    else:
        l3 = customtkinter.CTkLabel(master=frame, text="Pseudo ou mot de passe incorrect.", font=('Century Gothic', 12))
        l3.place(x=90, y=195)
        print("Pseudo ou mot de passe incorrect.")

def button_function2():
app.destroy()
subprocess.Popen(["python", "page_inscription.py"])

frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Se Connecter", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Pseudo')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=login, corner_radius=6)
button1.place(x=50, y=240)

button2 = customtkinter.CTkButton(master=frame, width=220, text="S'inscrire", command=button_function2,
                                  corner_radius=6)
button2.place(x=50, y=280)

app.mainloop()
