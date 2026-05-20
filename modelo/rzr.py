from modelo.vehiculo import Vehiculo


class RZR(Vehiculo):

    def __init__(
        self,
        modelo,
        precio,
        tipo,
        cantidad,
        activo=True
    ):

        super().__init__(
            modelo,
            precio
        )

        self._tipo = tipo
        self._cantidad = cantidad
        self._activo = activo


    def get_tipo(self):
        return self._tipo

    def get_cantidad(self):
        return self._cantidad

    def get_activo(self):
        return self._activo

 
    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_activo(self, activo):
        self._activo = activo

    
    def disminuir_cantidad(self):

        if self._cantidad > 0:
            self._cantidad -= 1


    def calcular_precio(self):

        return self._precio