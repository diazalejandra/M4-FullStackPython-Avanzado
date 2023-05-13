class Padre:
    atributo_clase = 10

    def __init__(self, name, rut_padre):
        self.name = name
        self.rut = rut_padre
        self.sueldo = 0
    
    def pintar(self):
        print(f"{self.name} está pintando.")

class Hijo(Padre):
    def __init__(self, nombre_hijo, rut_hijo, color_ojos):
        Padre.__init__(self, nombre_hijo, rut_hijo)
        self.color_ojos = color_ojos
    
    def lijar(self):
        print(f"{self.name} está lijando.")

richar = Padre("Richar Lujano", "1")
richard = Hijo("Richard Lujano", "2", "Marrón")

print(richar.name, richar.sueldo)
print(richard.name, richard.sueldo, richar.atributo_clase)
richard.sueldo = 20
print(richard.name, richard.sueldo, richard.atributo_clase)

richar.pintar()
richard.pintar()
richard.lijar()
