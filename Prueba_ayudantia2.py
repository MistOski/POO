class Trabajador():
    def __init__(self, nombre):
        self.nombre = nombre
    def tarea(self):
        print("Labores generales")
    
class Chef(Trabajador): #Se hereda la clase de trabajador
    def __init__(self, especialidad, nombre):
        Trabajador().__init__(especialidad, nombre)    
        self.especialidad = "Cocinero"
        self.nombre = "Tomas"

class Mesero(Trabajador): #Se hereda la clase de trabajador
    def __init__(self, especialidad, nombre, seccion):
        Trabajador().__init__(especialidad, nombre)
        self.nombre = "Elliot"
        self.seccion = "Comedor" 
        self.especialidad = "Mesero"
    
class AyudanteChefMesero(Chef, Mesero): #Hereda el rol de chef y mesero
    def __init__(self, especialidad, nombre):
        Chef().__init__(especialidad, nombre)
        Mesero().__init__(especialidad, nombre)

