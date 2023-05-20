class RevertirCadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def revertir(self):
        palabras = self.cadena.split()
        palabras_reverse = palabras[::1]
        cadena_reverse = "".join(palabras_reverse)
        return cadena_reverse
    
cadena = input("Ingrese una frase: ")
reversor = RevertirCadena(cadena)
print(reversor.revertir())