from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return pi * (self.radio ** 2)

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return 0.5 * self.base * self.altura

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado * self.lado

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    def calcular_area(self):
        return 0.5 * (self.base_mayor + self.base_menor) * self.altura

class PentagonoRegular:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema
    def calcular_area(self):
        perimetro = 5 * self.lado
        return 0.5 * perimetro * self.apotema

def mostrar_area(figura):
    try:
        area = figura.calcular_area()
        print(f"Area: {area}")
        return area
    except Exception as e:
        print("El objeto no tiene calcular_area o hubo error:", e)
        raise

mostrar_area(Circulo(3))
mostrar_area(Rectangulo(4,5))
mostrar_area(Triangulo(4,5))
mostrar_area(Cuadrado(3))
mostrar_area(Trapecio(6,4,3))
mostrar_area(PentagonoRegular(2,1.376))  # aprox apotema
print()
