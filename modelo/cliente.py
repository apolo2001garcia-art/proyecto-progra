class Cliente:

    def __init__(self, nombre, telefono, correo):
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo

    def get_nombre(self):
        return self._nombre

    def get_telefono(self):
        return self._telefono

    def get_correo(self):
        return self._correo
    