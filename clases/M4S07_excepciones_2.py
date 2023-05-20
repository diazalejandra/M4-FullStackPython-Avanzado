class NoPuedeEscribirDosException(Exception):
    def __init__(self, message):
        self.message = message

try:
    number = input("Introduce un numero: ")
    if (number == "2"):
        raise NoPuedeEscribirDosException("Introdujo un número 2 y este no es válido")
    else:
        print("Número introducido correctamente")
except Exception as error:
    print(type(error))
    print(error.args)