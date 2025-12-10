#Una empresa está desarrollando un sistema de gestión de pagos para su plataforma
#de comercio electrónico. La plataforma admite diferentes métodos de pago, como
#pago tiene un comportamiento diferente. Por ejemplo:

#1.Las tarjetas de crédito necesitan ser validadas antes de procesar el pago.

#2.Las transferencias bancarias requieren un código de confirmación antes de completar la transacción.

#3.Los pagos en efectivo no necesitan validación ni confirmación, solo deben registrar el monto recibido.

#Actualmente, la clase base MetodoDePago() incluye un método procesar_pago() que
#asume que todos los métodos de pago deben validarse antes de procesarse. Sin
#embargo, este diseño está causando problemas, ya que los pagos en efectivo no
#necesitan validación, y algunos métodos de pago están lanzando excepciones inesperadas

#El sistema actual viola el Principio de Sustitución de Liskov (LSP) porque no todos los
#métodos de pago respetan el comportamiento esperado de la clase base.
#Tu tarea es rediseñar la jerarquía de clases para que los métodos de pago cumplan
#con el LSP, asegurando que las subclases puedan ser utilizadas de forma
#intercambiable sin romper el programa.










