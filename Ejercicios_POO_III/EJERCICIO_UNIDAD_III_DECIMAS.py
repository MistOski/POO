class Animal:
    def __init__(self, nombre, edad, kg=None):
        self.nombre = nombre
        self.edad = edad
        self.kg = kg
    def comer (self):
        print(f"{self.nombre} esta comiendo")
    
    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

    def mostrarficha(self):
        info = f"Nombre: {self.nombre}, Edad: {self.edad}"
        if self.kg is not None:
            info += f", Peso: {self.kg} kg"
        print(info)

class Perro(Animal):
    def __init__(self, nombre, edad, raza, kg=None):
        super().__init__(nombre, edad, kg)
        self.raza = raza
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

class Gato(Animal):
    def __init__(self, nombre, edad, color, pelaje, kg=None):
        super().__init__(nombre, edad, kg)
        self.color = color
        self.pelaje = pelaje
    def maullar(self):
        print(f"{self.nombre} esta maullando")

