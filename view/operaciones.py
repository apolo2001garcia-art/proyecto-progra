import customtkinter as ctk
from tkinter import messagebox


class VentanaOperaciones(ctk.CTkToplevel):

    def __init__(self, parent, agencia, excel):
        super().__init__(parent)

        self.focus()
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))

        self.title("Operaciones")
        self.geometry("500x500")

        self.agencia = agencia
        self.excel = excel

       

        ctk.CTkLabel(
            self,
            text="Rentas y Ventas",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

       

        clientes = [

            c.get_nombre()

            for c in self.agencia.obtener_clientes()
        ]

        if not clientes:
            clientes = ["Sin clientes"]

        self.cliente = ctk.CTkComboBox(
            self,
            values=clientes
        )

        self.cliente.pack(pady=5)

      

        modelos = [

            r.get_modelo()

            for r in self.agencia.obtener_rzrs()

            if r.get_cantidad() > 0
        ]

        if not modelos:
            modelos = ["Sin vehículos"]

        self.vehiculo = ctk.CTkComboBox(
            self,
            values=modelos
        )

        self.vehiculo.pack(pady=5)

   

        self.operacion = ctk.CTkComboBox(
            self,
            values=[
                "Renta",
                "Venta"
            ],
            command=self.actualizar_tipo
        )

        self.operacion.pack(pady=5)

      

        self.dias = ctk.CTkEntry(
            self,
            placeholder_text="Días (solo renta)"
        )

        self.dias.pack(pady=5)

      

        ctk.CTkButton(
            self,
            text="Calcular Precio",
            command=self.calcular_precio
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="Registrar Operación",
            command=self.registrar_operacion
        ).pack(pady=10)

   

    def actualizar_tipo(self, opcion):

        if opcion == "Venta":

            self.dias.configure(
                state="disabled"
            )

        else:

            self.dias.configure(
                state="normal"
            )

   

    def calcular_precio(self):

        modelo = self.vehiculo.get()

        tipo_operacion = self.operacion.get()

        rzr = self.agencia.buscar_rzr(modelo)

        if rzr is None:

            messagebox.showerror(
                "Error",
                "Vehículo no encontrado"
            )

            return

        precio_base = rzr.get_precio()

    

        if tipo_operacion == "Venta":

            messagebox.showinfo(
                "Precio",
                f"Precio de venta: ${precio_base}"
            )

    

        elif tipo_operacion == "Renta":

            dias_texto = self.dias.get()

            if dias_texto == "":

                messagebox.showerror(
                    "Error",
                    "Ingresa los días"
                )

                return

            try:

                dias = int(dias_texto)

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Días inválidos"
                )

                return

            if dias <= 0:

                messagebox.showerror(
                    "Error",
                    "Los días deben ser mayores a 0"
                )

                return

            precio_renta = precio_base * 0.01 * dias

            messagebox.showinfo(
                "Precio",
                f"Renta por {dias} días: ${precio_renta}"
            )
    

    def registrar_operacion(self):

        cliente = self.cliente.get()
        vehiculo = self.vehiculo.get()
        operacion = self.operacion.get()

      

        if cliente == "Sin clientes":

            messagebox.showerror(
                "Error",
                "No hay clientes registrados"
            )

            return

        if vehiculo == "Sin vehículos":

            messagebox.showerror(
                "Error",
                "No hay vehículos registrados"
            )

            return

        rzr = self.agencia.buscar_rzr(vehiculo)

        if rzr is None:

            messagebox.showerror(
                "Error",
                "Vehículo no encontrado"
            )

            return

        precio_base = rzr.get_precio()

        

        if operacion == "Venta":

            precio = precio_base

            if rzr.get_cantidad() <= 0:

                messagebox.showerror(
                    "Error",
                    "No hay unidades disponibles"
                )

                return

           
            rzr.disminuir_cantidad()

          
            self.excel.actualizar_rzr(rzr)

       

        else:

            dias_texto = self.dias.get()

            if dias_texto == "":

                messagebox.showerror(
                    "Error",
                    "Ingresa los días"
                )

                return

            try:

                dias = int(dias_texto)

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Días inválidos"
                )

                return

            precio = precio_base * 0.01 * dias

        

        self.excel.guardar_operacion(
            cliente,
            vehiculo,
            operacion,
            precio
        )

        messagebox.showinfo(
            "Éxito",
            "Operación registrada"
        )