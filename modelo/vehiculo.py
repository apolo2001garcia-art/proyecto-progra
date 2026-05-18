from abc import ABC, abstractmethod


class Vehiculo(ABC):

    def __init__(self, modelo, precio, tipo, cantidad):

        self._modelo = modelo
        self._precio = precio
        self._tipo = tipo
        self._cantidad = cantidad

  

    def get_modelo(self):
        return self._modelo

    def get_precio(self):
        return self._precio

    def get_tipo(self):
        return self._tipo

    def get_cantidad(self):
        return self._cantidad

  

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_precio(self, precio):
        self._precio = precio

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

  
    @abstractmethod
    def calcular_precio(self):
        pass