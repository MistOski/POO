from abc import ABC, abstractmethod
from typing import List

class Vehiculo(ABC):
    @abstractmethod
    def moverse(self):
        pass

class Terrestre(Vehiculo):
    def rodar(self):
        print("rodando por la pista")

    def moverse(self):
        self.rodar()

class Acuatico(Vehiculo):
    def navegar(self):
        print("navegando en el agua")

    def moverse(self):
        self.navegar()

class Aereo(Vehiculo):
    def volar(self):
        print("volando por el aire")

    def moverse(self):
        self.volar()

class Coche(Terrestre):
    def __init__(self, nombre):
        self.nombre = nombre

    def rodar(self):
        print(f"{self.nombre}: rodar (coche)")

class Lancha(Acuatico):
    def __init__(self, nombre):
        self.nombre = nombre

    def navegar(self):
        print(f"{self.nombre}: navegar (lancha)")

class VehiculoAnfibio(Terrestre, Acuatico):
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        # primero rueda luego navega
        print(f"{self.nombre}: anfibio se mueve")
        self.rodar()
        self.navegar()

    def rodar(self):
        print(f"{self.nombre}: rodar (anfibio)")

    def navegar(self):
        print(f"{self.nombre}: navegar (anfibio)")

class Hidroavion(Acuatico, Aereo):
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        print(f"{self.nombre}: hidroavion se mueve")
        self.navegar()
        self.volar()

    def navegar(self):
        print(f"{self.nombre}: navegar (hidroavion)")

    def volar(self):
        print(f"{self.nombre}: volar (hidroavion)")

competidores: List[Vehiculo] = [
    Coche("Coche A"),
    Lancha("Lancha B"),
    VehiculoAnfibio("Anfibio C"),
    Hidroavion("Hidroavion D")
]

for v in competidores:
    v.moverse()
print()
