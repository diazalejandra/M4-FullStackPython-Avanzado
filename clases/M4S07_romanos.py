import math
class Romanos:
    valores = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
    simbolos = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
    
    def __init__(self, num):
        self.num = num
    
    def convertir_a_romano(self):
        resultado = ""
        i = 0
        while self.num > 0:
            if self.num >= self.valores[i]:
                resultado += self.simbolos[i]
                self.num -= self.valores[i]
            else:
                i += 1
        return resultado

# Ejemplo de uso
numero = 1234
convertido = Romanos(numero)
numero_romano = convertido.convertir_a_romano()
print(numero_romano)