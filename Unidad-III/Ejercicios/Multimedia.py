from abc import ABC, abstractmethod

class ArchivoMultimedia:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño  # en KB por ejemplo

class Reproducible(ABC):
    @abstractmethod
    def reproducir(self):
        pass

class Audio(ArchivoMultimedia, Reproducible):
    def __init__(self, nombre, tamaño, duracion):
        super().__init__(nombre, tamaño)
        self.duracion = duracion
    def reproducir(self):
        print(f"Reproduciendo audio {self.nombre} duracion {self.duracion}")

class Video(ArchivoMultimedia, Reproducible):
    def __init__(self, nombre, tamaño, duracion, resolucion):
        super().__init__(nombre, tamaño)
        self.duracion = duracion
        self.resolucion = resolucion
    def reproducir(self):
        print(f"Reproduciendo video {self.nombre} resolucion {self.resolucion} duracion {self.duracion}")

class Imagen(ArchivoMultimedia):
    def __init__(self, nombre, tamaño, formato):
        super().__init__(nombre, tamaño)
        self.formato = formato
    def mostrar(self):
        print(f"Mostrando imagen {self.nombre} formato {self.formato}")

def reproductor_automatico(item):
    if not isinstance(item, Reproducible):
        raise TypeError("objeto no reproducible")
    item.reproducir()

print("=== Pruebas multimedia LSP ===")
a = Audio("cancion.mp3", 4000, "3:20")
v = Video("clip.mp4", 50000, "2:10", "1080p")
img = Imagen("foto.jpg", 1200, "jpg")

reproductor_automatico(a)
reproductor_automatico(v)
try:
    reproductor_automatico(img)
except TypeError as e:
    print("Error esperado:", e)
print()