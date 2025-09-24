class Persona:
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura  
        self.peso = peso      

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"{self.nombre} {self.apellido} tiene un IMC de {imc:.2f}")
        
        if imc < 18.5:
            print("Está en BAJO PESO")
        elif 18.5 <= imc < 25:
            print("Está en un PESO NORMAL")
        elif 25 <= imc < 30:
            print("Está en SOBREPESO")
        else:
            print("Está en OBESIDAD")
        
        return imc

    def promedio_asignatura(self, nota1, nota2, nota3):
        promedio = (nota1 + nota2 + nota3) / 3
        print(f"El promedio de {self.nombre} es: {promedio:.2f}")
        
        if promedio >= 4.0:
            print("Aprobo la asignatura")
        else:
            print("No aprobo la asignatura")
        
        return promedio


# Ejemplo de uso:
persona1 = Persona("Ignacio", "Millapani", 20, 1.73, 65)

persona1.calcular_imc()
persona1.promedio_asignatura(5.0, 3.5, 4.5)