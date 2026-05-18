import customtkinter as ctk
from tkinter import messagebox


class VentanaVehiculos(ctk.CTkToplevel):

    def __init__(self, parent, agencia, excel):
        super().__init__(parent)

        self.focus()
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))

        self.agencia = agencia
        self.excel = excel

        self.title("Vehículos")
        self.geometry("500x550")

       

        ctk.CTkLabel(
            self,
            text="Administrar RZR",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

       

        modelos = [

            r.get_modelo()

            for r in self.agencia.obtener_rzrs()
        ]

        if not modelos:
            modelos = ["Sin vehículos"]

        self.lista = ctk.CTkComboBox(
            self,
            values=modelos,
            command=self.cargar_datos
        )

        self.lista.pack(pady=10)

    

        self.modelo = ctk.CTkEntry(
            self,
            placeholder_text="Modelo"
        )

        self.modelo.pack(pady=5)

        

        self.precio = ctk.CTkEntry(
            self,
            placeholder_text="Precio"
        )

        self.precio.pack(pady=5)

      

        self.tipo = ctk.CTkComboBox(
            self,
            values=[
                "Deportivo",
                "Utilitario",
                "Familiar"
            ]
        )

        self.tipo.pack(pady=5)

      

        self.cantidad = ctk.CTkEntry(
            self,
            placeholder_text="Cantidad"
        )

        self.cantidad.pack(pady=5)

       

        ctk.CTkButton(
            self,
            text="Guardar Cambios",
            command=self.guardar_cambios
        ).pack(pady=10)

       

        ctk.CTkButton(
            self,
            text="Eliminar Vehículo",
            fg_color="red",
            hover_color="darkred",
            command=self.eliminar_vehiculo
        ).pack(pady=10)

    

    def cargar_datos(self, modelo):

        rzr = self.agencia.buscar_rzr(modelo)

        if rzr is None:
            return

        self.rzr_actual = rzr

       
        self.modelo.delete(0, "end")
        self.modelo.insert(
            0,
            rzr.get_modelo()
        )

       
        self.precio.delete(0, "end")
        self.precio.insert(
            0,
            str(rzr.get_precio())
        )

       
        self.tipo.set(
            rzr.get_tipo()
        )

       
        self.cantidad.delete(0, "end")
        self.cantidad.insert(
            0,
            str(rzr.get_cantidad())
        )

    

    def guardar_cambios(self):

        try:

            modelo = self.modelo.get()

            precio = float(
                self.precio.get()
            )

            tipo = self.tipo.get()

            cantidad = int(
                self.cantidad.get()
            )

           

            if modelo == "":

                messagebox.showerror(
                    "Error",
                    "Modelo vacío"
                )

                return

            if cantidad < 0:

                messagebox.showerror(
                    "Error",
                    "Cantidad inválida"
                )

                return

            

            self.rzr_actual.set_modelo(
                modelo
            )

            self.rzr_actual.set_precio(
                precio
            )

            self.rzr_actual.set_tipo(
                tipo
            )

            self.rzr_actual.set_cantidad(
                cantidad
            )

           

            self.excel.actualizar_rzr(
                self.rzr_actual
            )

            messagebox.showinfo(
                "Éxito",
                "Vehículo actualizado"
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Precio o cantidad inválidos"
            )

   

    def eliminar_vehiculo(self):

        if not hasattr(self, "rzr_actual"):

            messagebox.showerror(
                "Error",
                "Selecciona un vehículo"
            )

            return

        modelo = self.rzr_actual.get_modelo()

        

        self.agencia.eliminar_rzr(modelo)

        

        self.excel.eliminar_rzr(modelo)

        messagebox.showinfo(
            "Éxito",
            "Vehículo eliminado"
        )

        self.destroy()