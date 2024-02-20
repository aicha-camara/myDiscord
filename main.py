# importer tkinter
import tkinter

# definir une fonction pour envoyer un message
def send_message():
    message_content = enter_message_box_var.get()  # recupere le message

    if message_content:
        message_list_box.insert("end", f"{pseudo} : {message_content}")  # l'affiche sur la boite
        enter_message_box_var.set("")


# Definir des constantes
MAIN_COLOR = "#424549"
SECONDARY_COLOR = "#36393e"
pseudo = "Aicha"

# creer une fenetre
root = tkinter.Tk()
root.title("Mini discord")
root.geometry("1080x720")  # changer taille fenetre

# configurer la taille des grilles
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)

# creer une boite à gauche
subframe = tkinter.Frame(root, bg=MAIN_COLOR)
channels_list = tkinter.Listbox(subframe, bg=MAIN_COLOR, fg='red', font=("Arial", 20))
channels_list.insert(0, "#general")
channels_list.insert(1, "#aide")
channels_list.insert(2, "#support")
channels_list.pack(fill='both', expand='yes')
subframe.grid(row=0, column=0, sticky='nsew')

# creer une boite à droite
subframe2 = tkinter.Frame(root, bg=SECONDARY_COLOR)

# zone ou on voit tout les messages
message_list_box = tkinter.Listbox(subframe2, bg=SECONDARY_COLOR, font=("Arial", 30, "italic"))
message_list_box.insert(0, "Bienvenue sur le chat ")
message_list_box.pack(fill='both', expand='yes',)

# zone pour ecrire un nouveau message
enter_message_box_var = tkinter.StringVar()
enter_message_box_var.set("Saisir votre message")

enter_message_box = tkinter.Entry(subframe2, bg=SECONDARY_COLOR, textvariable=enter_message_box_var, font=("Arial", 20))
enter_message_box.pack(fill='both', )
enter_message_box.bind("<FocusIn>", lambda event: enter_message_box_var.set(""))

# un bouton pour envoyer le nouveau message
submit_button = tkinter.Button(subframe2, text='Envoyer', command=send_message)
submit_button.pack(fill='both')

subframe2.grid(row=0, column=1, sticky='nsew')

# maintenir la fenetre allumé
root.mainloop()