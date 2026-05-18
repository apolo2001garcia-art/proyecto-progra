from modelo.vehiculo import Vehiculo


class RZR(Vehiculo):

    def __init__(self, modelo, precio, tipo, cantidad):

        super().__init__(
            modelo,
            precio,
            tipo,
            cantidad
        )

  

    def disminuir_cantidad(self):

        if self._cantidad > 0:
            self._cantidad -= 1


    def calcular_precio(self):

        return self._precio