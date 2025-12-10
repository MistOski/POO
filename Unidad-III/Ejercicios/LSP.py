from abc import ABC, abstractmethod

class MetodoDePago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

class Validable(ABC):
    @abstractmethod
    def validar(self):
        pass

class Confirmable(ABC):
    @abstractmethod
    def confirmar(self, codigo):
        pass

class TarjetaCredito(MetodoDePago, Validable):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.validado = False

    def validar(self):
        if len(str(self.numero)) >= 12:
            self.validado = True
        else:
            self.validado = False
        return self.validado

    def procesar_pago(self, monto):
        if not self.validado:
            ok = self.validar()
            if not ok:
                raise ValueError("tarjeta no valida")
        print(f"Pago con tarjeta por {monto} procesado para {self.titular}")

class Transferencia(MetodoDePago, Confirmable):
    def __init__(self, cuenta_origen, cuenta_destino):
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.confirmada = False

    def confirmar(self, codigo):
        self.confirmada = (codigo == "OK")
        return self.confirmada

    def procesar_pago(self, monto):
        if not self.confirmada:
            raise ValueError("transferencia no confirmada")
        print(f"Transferencia por {monto} de {self.cuenta_origen} a {self.cuenta_destino} completada")

class Efectivo(MetodoDePago):
    def __init__(self):
        self.registro = []

    def procesar_pago(self, monto):

        self.registro.append(monto)
        print(f"Efectivo recibido: {monto}")

tc = TarjetaCredito(123456789012, "Alumno")
try:
    tc.procesar_pago(1000)
except ValueError as e:
    print("Error tarjeta:", e)

tr = Transferencia("cuentaA", "cuentaB")
try:
    tr.procesar_pago(2000)
except ValueError as e:
    print("Error transferencia:", e)

tr.confirmar("OK")
tr.procesar_pago(2000)

ef = Efectivo()
ef.procesar_pago(500)
print()