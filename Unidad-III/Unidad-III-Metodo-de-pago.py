class MetodoDePago:
    def procesar_pago(self, monto):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")


class TarjetaCredito(MetodoDePago):
    def validar_tarjeta(self):
        return True
    
    def procesar_pago(self, monto):
        if not self.validar_tarjeta():
            return "Pago rechazado, tarjeta invalida"
        return f"Pago procesado con tarjeta por {monto}"


class TransferenciaBancaria(MetodoDePago):
    def confirmar_codigo(self, codigo):
        return codigo == "OK"

    def procesar_pago(self, monto):
        if not self.confirmar_codigo("OK"):
            return "Transferencia rechazada"
        return f"Transferencia completada por {monto}"


class PagoEfectivo(MetodoDePago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo registrado por {monto}"







