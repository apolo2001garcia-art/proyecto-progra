import customtkinter as ctk
from view.interfaz import App

# Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Ejecutar app
app = App()
app.mainloop()