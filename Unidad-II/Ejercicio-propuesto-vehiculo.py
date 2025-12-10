class Vehiculo:
    def __init__(self, marca, modelo, año):
 
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True
    
    def marcar_vendido(self):
        self.__disponible = False
    
    def __str__(self):
        estado = "Disponible" if self.__disponible else "No disponible"
        return f"{self.__marca} {self.__modelo} {self.__año} | {estado}"
    
class Concesionaria:
    
    def __init__(self):
        # Lista publica de vehiculos
        self.vehiculos = []
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
    
    def mostrar_vehiculos(self):
        print("Vehiculos disponibles:")
        for v in self.vehiculos:
            print(" -", v)
    
    def vender_vehiculo(self, indice):
        if indice < 0 or indice >= len(self.vehiculos):
            print("Indice no valido")
            return
        
        vehiculo = self.vehiculos[indice]

        if "No disponible" in str(vehiculo):
            print("El vehiculo ya fue vendido")
        else:
            vehiculo.marcar_vendido()
            print("Vehiculo vendido con exito")

v1 = Vehiculo("Toyota", "Corolla", 2019)
v2 = Vehiculo("Nissan", "Versa", 2020)

c = Concesionaria()
c.agregar_vehiculo(v1)
c.agregar_vehiculo(v2)

c.mostrar_vehiculos()
c.vender_vehiculo(0)

c.mostrar_vehiculos()

