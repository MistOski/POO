class Gatos:
    def __init__(self, nombre, edad, hambre, energia):
        self.nombre = nombre
        self.edad = edad
        self.hambre = hambre
        self.energia = energia

    def juego(self, pelota=20, rascadores=10):
        self.energia -= pelota
        self.hambre += rascadores

    def comida(self, galletas=20, pescado=80):
        self.hambre -= galletas
        self.energia += galletas // 2
        self.hambre -= pescado
        self.energia += pescado // 2

    def __str__(self):
        return f"Gato(nombre={self.nombre}, edad={self.edad}, hambre={self.hambre}, energia={self.energia})"

    def __del__(self):
        print(f"El gato {self.nombre} ha salido del cafe")


gato1 = Gatos("michi", 2, 47, 80)
gato2 = Gatos("michigan", 3, 70, 94)

print(f"{gato1}, {gato2}")


class Cafe:
    def __init__(self, nombre, capacidad_maxima):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.gatos_presentes = []

    def agregar_gato(self, gato):
        if len(self.gatos_presentes) < self.capacidad_maxima:
            self.gatos_presentes.append(gato)
        else:
            print(f"No se puede agregar mas gatos al {self.nombre}, capacidad maxima alcanzada.")

    def mostrar_gatos(self):
        for gato in self.gatos_presentes:
            print(f"Nombre: {gato.nombre}, Edad: {gato.edad}, Hambre: {gato.hambre}, Energia: {gato.energia}")
