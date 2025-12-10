class Vehiculo:
    def _vehiculo(self, marca, modelo, año, disponible):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
    def marcar_vendido(self, disponible):
        if self.__disponible:
           self.__disponible = False
           print("El modelo esta disponible")
        else:
           print("El vehiculo no esta disponible")
    def __str__(self):
        estado = "Disponible" if self.__disponible else ("No esta disponible")

        


