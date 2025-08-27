class animal():
    #Constructor de clase animal
    #Atributos de clase animal compartidos por varias especies
    def __init__(self, nombre, especie):
        self.nombre = nombre  #Self permite referirse a los atributos a la hora de llamarlos en el codigo
        self.especie = especie

    def correr(self):
        print(f"{self.nombre} está corriendo.")

#Creación de un objeto de la clase animal y comprobando sus atributos
gatito = animal("Michi", "Gato")
print(f"El nombre del animal es {gatito.nombre} y es un {gatito.especie}.")

#Llamada al método correr
gatito.correr()