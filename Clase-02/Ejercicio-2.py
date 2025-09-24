class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = gasolina   # Seran los litros disponibles de gasolina
        self.kilometros_recorridos = 0   # Se empieza desde el inicio (0)

    def conducir(self, km):
        km_posibles = self.gasolina * 10  #Se le asigna el rendimiento a la gasolina

        if km <= km_posibles:
            self.kilometros_recorridos += km  #Situacion donde el vehiculo alcanza a recorrer todo
            self.gasolina -= km / 10
            print(f"El coche {self.marca} recorrio {km} km.")
        else:
            self.kilometros_recorridos += km_posibles
            self.gasolina = 0  #Situacion donde el vehiculo no alcanzo los kilometros propuestos pero se mencionan los recorridos
            print(f"El coche {self.marca} recorrio {km_posibles} km y se quedo sin gasolina.")

    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Se cargaron {litros} litros de gasolina. Ahora tiene {self.gasolina} litros.")


# Ejemplo de uso
mi_coche = Coche("Toyota", 5)   
mi_coche.conducir(30)         
mi_coche.conducir(40)          
mi_coche.cargar_gasolina(10)    
mi_coche.conducir(70)          