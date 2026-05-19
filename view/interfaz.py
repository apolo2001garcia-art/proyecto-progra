import customtkinter as ctk
from tkinter import messagebox

from view.clientes import VentanaClientes
from view.operaciones import VentanaOperaciones
from view.estadisticas import VentanaEstadisticas

from controller.agencia import Agencia

from datos.excel_manager import ExcelManager

from modelo.rzr import RZR



class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("RZR Manager")
        self.geometry("1000x650")

        self.agencia = Agencia()
        self.excel = ExcelManager()

        

        clientes_guardados = self.excel.cargar_clientes()

        for c in clientes_guardados:
            self.agencia.agregar_cliente(c)

        rzrs_guardados = self.excel.cargar_rzrs()

        for r in rzrs_guardados:
            self.agencia.agregar_rzr(r)

        

        titulo = ctk.CTkLabel(
            self,
            text="🏎️ RZR MANAGER",
            font=("Arial", 38, "bold")
        )

        titulo.pack(pady=25)

        

        frame = ctk.CTkFrame(
            self,
            corner_radius=20
        )

        frame.pack(
            padx=40,
            pady=20,
            fill="both",
            expand=True
        )

       

        subtitulo = ctk.CTkLabel(
            frame,
            text="Registrar Nuevo Vehículo",
            font=("Arial", 24, "bold")
        )

        subtitulo.pack(pady=20)

        self.modelo = ctk.CTkEntry(
            frame,
            placeholder_text="Modelo",
            width=300,
            height=40
        )

        self.modelo.pack(pady=10)

        self.precio = ctk.CTkEntry(
            frame,
            placeholder_text="Precio",
            width=300,
            height=40
        )

        self.precio.pack(pady=10)

        self.tipo = ctk.CTkComboBox(
            frame,
            values=[
                "Deportivo",
                "Utilitario",
                "Familiar"
            ],
            width=300,
            height=40
        )

        self.tipo.pack(pady=10)

        self.cantidad = ctk.CTkEntry(
            frame,
            placeholder_text="Cantidad disponible",
            width=300,
            height=40
        )

        self.cantidad.pack(pady=10)

        

        botones = ctk.CTkFrame(
            frame,
            fg_color="transparent"
        )

        botones.pack(pady=25)

        ctk.CTkButton(
            botones,
            text="Agregar RZR",
            command=self.agregar_rzr,
            width=180,
            height=40,
            corner_radius=15
        ).grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkButton(
            botones,
            text="Ver RZR",
            command=self.abrir_rzrs,
            width=180,
            height=40,
            corner_radius=15
        ).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(
            botones,
            text="Clientes",
            command=self.abrir_clientes,
            width=180,
            height=40,
            corner_radius=15
        ).grid(row=1, column=0, padx=10, pady=10)

        ctk.CTkButton(
            botones,
            text="Operaciones",
            command=self.abrir_operaciones,
            width=180,
            height=40,
            corner_radius=15
        ).grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkButton(
            botones,
            text="Estadísticas",
            command=self.abrir_estadisticas,
            width=180,
            height=40,
            corner_radius=15
        ).grid(row=2, column=0, columnspan=2, pady=10)

    

    def abrir_clientes(self):

        VentanaClientes(
            self,
            self.agencia,
            self.excel
        )

    def abrir_operaciones(self):

        VentanaOperaciones(
            self,
            self.agencia,
            self.excel
        )

    def abrir_estadisticas(self):

        VentanaEstadisticas(self)

    def abrir_rzrs(self):

        from view.vehiculos import VentanaVehiculos

        VentanaVehiculos(
            self,
            self.agencia,
            self.excel
        )



    def agregar_rzr(self):

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

            

            rzr = RZR(
                modelo,
                precio,
                tipo,
                cantidad
            )

            

            if self.agencia.buscar_rzr(modelo) is None:

                
                self.agencia.agregar_rzr(rzr)

                
                self.excel.guardar_rzr(rzr)

                messagebox.showinfo(
                    "Éxito",
                    "RZR agregado correctamente"
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Ese modelo ya existe"
                )

            

            self.modelo.delete(0, "end")
            self.precio.delete(0, "end")
            self.cantidad.delete(0, "end")

        except ValueError:

            messagebox.showerror(
                "Error",
                "Precio o cantidad inválidos"
            )