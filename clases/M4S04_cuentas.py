class Cuenta():
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def imprimir_datos(self):
        print(f"Nombre titular {self.titular}, cantidad {self.cantidad}")

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    
class PlazoFijo(CajaAhorro):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
        