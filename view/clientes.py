import customtkinter as ctk
from tkinter import messagebox

from modelo.cliente import Cliente


class VentanaClientes(ctk.CTkToplevel):

    def __init__(self, parent, agencia, excel):
        super().__init__(parent)

        self.focus()
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))

        self.agencia = agencia
        self.excel = excel

        self.title("Clientes")
        self.geometry("450x400")

        

        ctk.CTkLabel(
            self,
            text="Registro de Clientes",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

       

        self.nombre = ctk.CTkEntry(
            self,
            placeholder_text="Nombre"
        )
        self.nombre.pack(pady=5)

        self.telefono = ctk.CTkEntry(
            self,
            placeholder_text="Teléfono"
        )
        self.telefono.pack(pady=5)

        self.correo = ctk.CTkEntry(
            self,
            placeholder_text="Correo"
        )
        self.correo.pack(pady=5)

        

        ctk.CTkButton(
            self,
            text="Agregar Cliente",
            command=self.agregar_cliente
        ).pack(pady=15)

    

    def agregar_cliente(self):

        nombre = self.nombre.get()
        telefono = self.telefono.get()
        correo = self.correo.get()

        
        if nombre == "":

            messagebox.showerror(
                "Error",
                "Nombre vacío"
            )

            return

        
        existente = self.agencia.buscar_cliente(nombre)

        if existente is not None:

            messagebox.showerror(
                "Error",
                "Ese cliente ya existe"
            )

            return

        
        cliente = Cliente(
            nombre,
            telefono,
            correo
        )

        
        self.agencia.agregar_cliente(cliente)

        
        self.excel.guardar_cliente(cliente)

        messagebox.showinfo(
            "Éxito",
            "Cliente agregado correctamente"
        )

        
        self.nombre.delete(0, "end")
        self.telefono.delete(0, "end")
        self.correo.delete(0, "end")