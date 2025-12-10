class Libreria:
    descuento_socios = 0.05  

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__catalogo = {}  
        self.__carrito = []   

    @property
    def catalogo(self):
        return self.__catalogo
    
    @classmethod
    def set_descuento(cls, nuevo_descuento):
        assert 0.05 <= nuevo_descuento <= 0.10, "Descuento fuera de rango"
        cls.descuento_socios = nuevo_descuento

    def agregar_libro_catalogo(self, titulo, precio):
        assert precio > 0, "El precio debe ser positivo"
        self.__catalogo[titulo] = precio
     
    def agregar_al_carrito(self, titulo):
        assert titulo in self.__catalogo, "El libro no existe en el catalogo"
        self.__carrito.append(titulo)

    @staticmethod
    def aplicar_descuento(monto, descuento):
        assert monto > 0, "Monto no valido"
        assert 0.05 <= descuento <= 0.10, "Descuento fuera de limites"
        return monto * (1 - descuento)
    
    def total_carrito(self, frecuente=False):
        total = 0

        for t in self.__carrito:
            assert t in self.__catalogo, "Carrito invalido"
            total += self.__catalogo[t]
        
        if frecuente:
            total = Libreria.aplicar_descuento(total, Libreria.descuento_socios)
        
        return total
    
    def __str__(self):
        return f"Libreria {self.__nombre} con {len(self.__catalogo)} libros"

lb = Libreria("Libreria Chiloe")

lb.agregar_libro_catalogo("El Principito", 8000)
lb.agregar_libro_catalogo("Cien Años de Soledad", 12000)
lb.agregar_libro_catalogo("Rayuela", 10000)

lb.agregar_al_carrito("El Principito")
lb.agregar_al_carrito("Rayuela")

print("Total sin descuento:", lb.total_carrito())
print("Total con descuento:", lb.total_carrito(frecuente=True))

Libreria.set_descuento(0.10)

print("Total con descuento maximo:", lb.total_carrito(frecuente=True))
