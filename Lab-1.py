#A. ¿Cómo representarías a los gatos dentro del sistema?
#¿Qué atributos crees que serían importantes para describir a un gato? 
#Piensa en atributos como el nombre, la edad, el nivel de energía y el nivel de hambre.
#Crea un constructor que inicialice estos atributos al momento de instanciar un objeto. 
class Gatos:
    def __init__(self, nombre, edad, hambre, energia): #Se agrego 'edad' como parametro requerido.
        self.nombre = nombre
        self.edad = edad
        self.hambre = hambre
        self.energia = energia

    # Método para jugar
    def juego(self, pelota=20, rascadores=10): #Se establecen valores 
        self.energia -= pelota
        self.hambre += rascadores

    # Método para alimentar
    def comida(self, galletas=20, pescado=80):
        self.hambre -= galletas
        self.energia += galletas // 2
        self.hambre -= pescado
        self.energia += pescado // 2

    def __str__(self):
        return f"Gato(nombre={self.nombre}, edad={self.edad}, hambre={self.hambre}, energia={self.energia})"
        return f"Gato(nombre={self.nombre}, hambre={self.hambre}, energia={self.energia})"

    # Finalizador
    def __del__(self):
        print(f"El gato {self.nombre} ha salido del café")
gato1 = Gatos("michi", 2, 47, 80)   #Se asignan los parametros actuales de los gatos, agregando edad.
gato2 = Gatos("michigan", 3, 70, 94)
gato2 = Gatos("michigan", 70, 94)

print(f"{gato1}, {gato2}")

#2. Espacios en el Café (30 Puntos) 

#A. ¿Cómo representarías los espacios dentro del café?
class Cafe: 
    def __init__(self, nombre, capacidad_maxima):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.gatos_presentes = []

    # Método para agregar un gato
    def agregar_gato(self, gato):
        if len(self.gatos_presentes) < self.capacidad_maxima:
            self.gatos_presentes.append(gato)
        else:
            print(f"No se puede agregar más gatos al {self.nombre}, capacidad máxima alcanzada.")

    def mostrar_gatos(self):
        for gato in self.gatos_presentes:
            print(f"Nombre: {gato.nombre}, Edad: {gato.edad}, Hambre: {gato.hambre}, Energía: {gato.energia}")
            print(f"Nombre: {gato.nombre}, Hambre: {gato.hambre}, Energía: {gato.energia}")

#¿Qué atributos serían importantes para describir un espacio del café? Piensa en atributos 
#como el nombre del espacio, la capacidad máxima de gatos que puede albergar, y una 
#lista de los nombres de los gatos presentes en ese espacio.

#Crea un constructor que inicialice estos atributos al momento de instanciar un objeto. 

#B. Métodos que necesita la clase Espacio:

#¿Cómo diseñarías un método que permita agregar un gato a un espacio del café? Debes 
#asegurarte de que no se exceda la capacidad máxima del área. 

#¿Cómo diseñarías un método que permita mostrar la información básica de los gatos 
#(nombre, edad) que se encuentran en cada espacio del café?

#3. Finalizador (20 puntos)
#A. Implementa un finalizador en la clase Gato que muestre un mensaje cuando un gato sea eliminado 
#del sistema (por ejemplo, “El gato [nombre] ha salido del café”)
    