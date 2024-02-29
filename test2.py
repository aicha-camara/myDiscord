import threading
import tkinter as tk
from PIL import ImageTk, Image
from client import Client

# Création de la fenêtre principale
app = tk.Tk()
app.geometry("1200x640")
app.title('discord')
MAIN_COLOR = "#282b30"

# Définition des paramètres d'apparence
app.tk_setPalette(background="#282b30", foreground="white")  # Couleur de fond et texte globaux
app.option_add("*Font", ("Century Gothic", 12))  # Police globale

# Charger l'image
img1 = ImageTk.PhotoImage(Image.open("assets/pattern.png"))
frame = tk.Label(master=app, image=img1)
frame.pack()

# Création boite gauche nom channel

subframe = tk.Frame(master=frame, width=320, height=600, bg=MAIN_COLOR)
subframe.place(relx=0.3, rely=0.5, anchor=tk.E)
l5 = tk.Label(master=subframe, text="LaPlateforme", font=('Century Gothic', 20), bg="blue")
l5.place(x=40, y=45)
button = tk.Button(master=subframe, width=30, text="General", )
button.place(x=20, y=120)
button = tk.Button(master=subframe, width=30, text="Image")
button.place(x=20, y=160)
button = tk.Button(master=subframe, width=30, text="Support")
button.place(x=20, y=200)
button = tk.Button(master=subframe, width=30, text="plainte")
button.place(x=20, y=240)

# Création boite droite textuel
subframe2 = tk.Frame(master=frame, width=700, height=600)
subframe2.place(relx=0.9, rely=0.5, anchor=tk.E)



app.mainloop()
