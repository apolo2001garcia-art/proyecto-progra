from abc import ABC, abstractmethod


class Vehiculo(ABC):

    def __init__(
        self,
        modelo,
        precio,
        disponible=True
    ):

        self._modelo = modelo
        self._precio = precio
        self._disponible = disponible

  
    def get_modelo(self):
        return self._modelo

    def get_precio(self):
        return self._precio

    def get_disponible(self):
        return self._disponible

 

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_precio(self, precio):
        self._precio = precio

    def set_disponible(self, disponible):
        self._disponible = disponible


    @abstractmethod
    def calcular_precio(self):
        pass