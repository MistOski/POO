class Gato:
    def __init__(self, nombre, id_mascota):

        self.nombre = nombre
        self.id_mascota = id_mascota


        self.__salud = "Saludable"
        self.__energia = 100
        self.__hambre = 0
        self.__historial = []

    def jugar(self):
        self.__energia -= 20
        self.__hambre += 15
        self.__registrar("El gato jugo")
        self.__actualizar_salud()

    def alimentar(self):
        self.__hambre -= 25
        self.__energia += 10
        self.__registrar("El gato fue alimentado")
        self.__actualizar_salud()

    def __registrar(self, texto):
        self.__historial.append(texto + " | Salud: " + self.__salud)

    def __actualizar_salud(self):
        if self.__energia <= 20 or self.__hambre >= 70:
            self.__salud = "En observacion"
        if self.__energia <= 5 or self.__hambre >= 90:
            self.__salud = "Enfermo"
        if self.__energia > 40 and self.__hambre < 50:
            self.__salud = "Saludable"

    def historial_medico(self):
        return self.__historial

    def __str__(self):
        return f"Gato {self.nombre} | Salud: {self.__salud} | Energia: {self.__energia} | Hambre: {self.__hambre}"

class Espacio:

    def __init__(self, nombre, capacidad):
      
        self.nombre = nombre
        self.capacidad = capacidad
       
        self.__gatos = []
        self.__conteo = 0

    def __actualizar_conteo(self):
        self.__conteo = len(self.__gatos)

    def agregar_gato(self, gato):
        if len(self.__gatos) < self.capacidad:
            self.__gatos.append(gato)
            self.__actualizar_conteo()
        else:
            print("El espacio esta lleno, no se puede agregar este gato")

    def reporte_area(self):
        print("Reporte del espacio:", self.nombre)
        print("Capacidad:", self.capacidad)
        print("Gatos presentes:", self.__conteo)
        print("Detalles:")
        for g in self.__gatos:
            print(" -", g)

    def __str__(self):
        return f"Espacio {self.nombre} con {self.__conteo} gatos"
    

g1 = Gato("Mishito", 20231)
g2 = Gato("Pelusa", 20232)

esp = Espacio("Sala Principal", 2)

esp.agregar_gato(g1)
esp.agregar_gato(g2)

g1.jugar()
g1.jugar()
g1.alimentar()

esp.reporte_area()

print("\nHistorial medico de", g1.nombre)
for evento in g1.historial_medico():
    print(evento)
