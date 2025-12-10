class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre

    def tarea(self):
        print("Labores generales")

class Chef(Trabajador):
    def __init__(self, nombre, especialidad, **kwargs):
        super().__init__(nombre, **kwargs)
        self.especialidad = especialidad

    def tarea(self):
        print(f"{self.nombre} prepara comida")


class Mesero(Trabajador):
    def __init__(self, nombre, seccion, **kwargs):
        super().__init__(nombre, **kwargs)
        self.seccion = seccion

    def tarea(self):
        print(f"{self.nombre} atiende mesas en {self.seccion}")


class AyudanteChefMesero(Chef, Mesero):
    def __init__(self, nombre, especialidad, seccion):
        super().__init__(nombre, especialidad=especialidad, seccion=seccion)

c = Chef("Tomas", "Cocina italiana")
m = Mesero("Elliot", "Comedor")
a = AyudanteChefMesero("Lucas", "Parrillas", "Terraza")

print(c.nombre, c.especialidad)
c.tarea()

print(m.nombre, m.seccion)
m.tarea()

print(a.nombre, a.especialidad, a.seccion)
a.tarea()