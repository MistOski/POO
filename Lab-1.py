#A. ¿Cómo representarías a los gatos dentro del sistema?
#¿Qué atributos crees que serían importantes para describir a un gato? 
#Piensa en atributos como el nombre, la edad, el nivel de energía y el nivel de hambre.
#Crea un constructor que inicialice estos atributos al momento de instanciar un objeto. 
class Gatos:
    def __init__(self, nombre, hambre, energia): #Se establecen los parametros requeridos para la identificacion del gato y su estado.
        self.nombre = nombre
        self.hambre = hambre
        self.energia = energia

gato1 = Gatos("michi", 47, 80)   #Se asignan los parametros actuales de los gatos.
gato2 = Gatos("michigan", 70, 94)

print(f"{gato1}, {gato2}")

#B. Métodos que necesita la clase Gato:
#¿Cómo diseñarías un método que permita que los gatos jueguen y cómo impactaría esto 
#en sus atributos como los niveles de energía y hambre?
     def juego(self, pelota=20, rascadores=10): #Se establecen valores 
           self.energia -= pelota
           self.hambre += rascadores
    
#¿Cómo diseñarías un método que permita alimentar a los gatos y restaurar sus niveles de energía y hambre. 
#C. Método Mágico: 
        def comida(self, galletas=20, pescado=80):
            self.hambre -= galletas
            self.energia += galletas // 2
            self.hambre -= pescado
            self.energia += pescado // 2

#Implementa un método que te permita imprimir de forma clara el estado del gato.
# ¿Qué información incluirías en la representación del gato?
        def __str__(self):
            return f"Gato(nombre={self.nombre}, hambre={self.hambre}, energia={self.energia})"
#2. Espacios en el Café (30 Puntos) 

#A. ¿Cómo representarías los espacios dentro del café?
        class Cafe: 
             def __init__(self, salon=10, terraza=20):
        
        
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
    