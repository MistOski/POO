class Contenido:
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio

    def mostrar_detalle(self):
        print("Titulo " + self.titulo)
        print("Anio " + str(self.anio))


class Reproducible:
    def reproducir(self):
        raise NotImplementedError("Subclase debe implementar reproducir")


class Calificable:
    def __init__(self):
        self.rating = 0.0

    def calificar(self, puntuacion):
        self.rating = puntuacion
        print("Nueva calificacion " + str(self.rating))


class Pelicula(Contenido, Reproducible):
    def __init__(self, titulo, anio, duracion_minutos):
        super().__init__(titulo, anio)
        self.duracion_minutos = duracion_minutos

    def reproducir(self):
        print("Reproduciendo pelicula " + self.titulo + " duracion minutos " + str(self.duracion_minutos))


class Documental(Contenido):
    def __init__(self, titulo, anio, tema):
        super().__init__(titulo, anio)
        self.tema = tema

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print("Tema " + self.tema)


class Miniserie(Contenido, Reproducible, Calificable):
    def __init__(self, titulo, anio, num_episodios):
        Contenido.__init__(self, titulo, anio)
        Calificable.__init__(self)
        self.num_episodios = num_episodios

    def reproducir(self):
        print("Reproduciendo miniserie " + self.titulo + " episodios " + str(self.num_episodios))


def lista_de_reproduccion(lista_contenidos):
    for contenido in lista_contenidos:
        if hasattr(contenido, "reproducir") and callable(getattr(contenido, "reproducir")):
            contenido.reproducir()
        else:
            print("El objeto no es reproducible " + contenido.titulo)


if __name__ == "__main__":
    pelicula = Pelicula("Matrix", 1999, 136)
    documental = Documental("Naturaleza", 2020, "Animales")
    miniserie = Miniserie("Ecos", 2023, 8)

    print("Prueba de LSP y Polimorfismo")
    lista_de_reproduccion([pelicula, documental, miniserie])

    print("Prueba de herencia multiple")
    miniserie.mostrar_detalle()
    miniserie.reproducir()
    miniserie.calificar(4.5)
