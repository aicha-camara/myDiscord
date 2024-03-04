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



