class Animal:
    def __init__(self, nombre, edad, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.genero = genero

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

    def mostrar_ficha(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso} kg, Genero: {self.genero}")

class Perro(Animal):
    def __init__(self, nombre, edad, peso, genero, raza):
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"Raza: {self.raza}")

class Gato(Animal):
    def __init__(self, nombre, edad, peso, genero, color_pelaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje

    def maullar(self):
        print(f"{self.nombre} esta maullando")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"Color pelaje: {self.color_pelaje}")

class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, genero, color_plumaje):
        super().__init__(nombre, edad, peso, genero)
        self.color_plumaje = color_plumaje

    def volar(self):
        print(f"{self.nombre} esta volando alto")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"Color plumaje: {self.color_plumaje}")

perro = Perro("Toby", 4, 12.5, "M", "Labrador")
gato = Gato("Michi", 2, 4.3, "F", "blanco y negro")
pajaro = Pajaro("Kiwi", 1, 0.12, "M", "verde")

perro.mostrar_ficha()
gato.mostrar_ficha()
pajaro.mostrar_ficha()
perro.ladrar()
gato.maullar()
pajaro.volar()

print()