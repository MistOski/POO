#Implementar una clase Fraccion que represente una fracción matemática con numerador y denominador. 
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    #Además se debe crear varios métodos mágicos que permitan operar, comparar, y mostrar las fracciones de manera intuitiva. 
    #La clase debe poseer los siguientes métodos mágicos:
    #Método mágico que devuelva la fracción como una representación de cadena
    def __str__(self): 
        return f"La fraccion en cadena: {self.numerador}, {self.denominador}"
    
    #Método mágico que permita sumar dos fracciones
    def __add__(self, fraccion):
        return Fraccion(
            self.numerador + fraccion.numerador,
            self.denominador + fraccion.denominador
        )
    
    #Método mágico que permita el producto entre dos fracciones
    def __mul__(self, fraccion):
        return Fraccion(
            self.numerador * fraccion.numerador,
            self.denominador * fraccion.denominador
        )
        
    #Método mágico que permita comparar dos fracciones. Dos fracciones se consideran iguales si sus valores numéricos son equivalentes.
    def __eq__(self, fraccion):
        return {self.numerador, self.denominador} == {fraccion.numerador, fraccion.denominador}

Fracciones = Fraccion #Se crea objeto

a = Fraccion(1, 2)
b = Fraccion(2, 4)

print(a + b)     # 8/8
print(a * b)     # 2/8
print(a == b)    # True
