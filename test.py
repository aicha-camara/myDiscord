import tkinter
import customtkinter
from PIL import ImageTk, Image

# Initialisation de CustomTkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# Création de la fenêtre principale
app = customtkinter.CTk()
app.geometry("1200x640")
app.title('discord')
MAIN_COLOR = "#282b30"
# Charger l'image
img1 = ImageTk.PhotoImage(Image.open("assets/pattern.png"))
frame = customtkinter.CTkLabel(master=app, image=img1)
frame.pack()

# Création boite gauche nom channel
subframe = customtkinter.CTkFrame(master=frame, width=320, height=600, corner_radius=15)
subframe.place(relx=0.3, rely=0.5, anchor=tkinter.E)
l5 = customtkinter.CTkLabel(master=frame, text="MON SERVEUR", font=('Century Gothic', 35), bg_color=MAIN_COLOR,                           corner_radius=30)
l5.place(x=40, y=45)
button = customtkinter.CTkButton(master=frame, width=300, text="General", corner_radius=6)
button.place(x=50, y=100)
button = customtkinter.CTkButton(master=frame, width=300, text="Image", corner_radius=6)
button.place(x=50, y=130)
button = customtkinter.CTkButton(master=frame, width=300, text="Support", corner_radius=6)
button.place(x=50, y=160)
button = customtkinter.CTkButton(master=frame, width=300, text="plainte", corner_radius=6)
button.place(x=50, y=190)

# Création boite droite textuel
subframe2 = customtkinter.CTkFrame(master=frame, width=700, height=600, corner_radius=15)
subframe2.place(relx=0.9, rely=0.5, anchor=tkinter.E)



app.mainloop()
