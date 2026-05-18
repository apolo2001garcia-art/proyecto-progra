from modelo.cliente import Cliente


class Agencia:

    def __init__(self):

        self.rzrs = []
        self.clientes = []
        self.ingresos = 0

   

    def agregar_rzr(self, rzr):

        self.rzrs.append(rzr)

    def eliminar_rzr(self, modelo):

        self.rzrs = [
            r for r in self.rzrs
            if r.get_modelo() != modelo
        ]

    def buscar_rzr(self, modelo):

        for r in self.rzrs:

            if r.get_modelo() == modelo:
                return r

        return None

    def obtener_rzrs(self):

        return self.rzrs

   

    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)

    def buscar_cliente(self, nombre):

        for c in self.clientes:

            if c.get_nombre() == nombre:
                return c

        return None

    def obtener_clientes(self):

        return self.clientes

    

    def registrar_venta(self, rzr):

        
        if rzr.get_cantidad() <= 0:
            return None

        
        nueva_cantidad = rzr.get_cantidad() - 1

        rzr.set_cantidad(nueva_cantidad)

        
        self.ingresos += rzr.get_precio()

        return rzr.get_precio()

    def registrar_renta(self, rzr, dias):

        
        if rzr.get_cantidad() <= 0:
            return None

        
        precio_renta = (
            rzr.get_precio() * 0.01
        ) * dias

        self.ingresos += precio_renta

        return precio_renta

    

    def calcular_ingresos(self):

        return self.ingresos
    