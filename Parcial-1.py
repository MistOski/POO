class Jugador:
    def __init__(self, nombre, edad, posicion, club, energia):
        self.__nombre = nombre
        self.__edad = edad
        self.__posicion = posicion
        self.__goles = 0

        self.club = club
        self.energia = energia
        posiciones_validas = ["DEL", "VOL", "DEF", "ARQ"]

        assert len(nombre) > 0
        assert club != ""
        assert edad >= 15
        assert posicion in posiciones_validas
        assert 0 <= energia <= 100
        assert self.__goles >= 0

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        assert len(nuevo_nombre) > 0
        self.__nombre = nuevo_nombre
        assert len(self.__nombre) > 0

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        assert nueva_edad >= 15
        self.__edad = nueva_edad
        assert self.__edad >= 15

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, nueva_posicion):
        posiciones_validas = ["DEL", "VOL", "DEF", "ARQ"]
        assert nueva_posicion in posiciones_validas
        self.__posicion = nueva_posicion
        assert self.__posicion in posiciones_validas

    @property
    def goles(self):
        return self.__goles

    def entrenar(self, minutos):
        assert minutos > 0
        self.energia -= minutos
        assert 0 <= self.energia <= 100

    def anotar_gol(self):
        self.__goles += 1
        assert self.__goles >= 0

    def __str__(self):
        return f"Jugador(nombre={self.__nombre}, club={self.club}, posicion={self.__posicion}, energia={self.energia}, goles={self.__goles})"


jugador1 = Jugador("Ignacio Millapani", 20, "DEL", "Club Castro", 75)
jugador1.club = "Club Mocopulli"
print(jugador1.club)
jugador1.energia = 40
print(jugador1.energia)

jugador1.entrenar(2)
print(jugador1.energia)

jugador2 = Jugador("Javier Neumann", 20, "DEF", "Club Dalcahue", 80)
jugador2.club = "Club Ancud"
print(jugador2.club)
jugador2.energia = 30
print(jugador2.energia)
