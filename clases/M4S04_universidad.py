class Persona():
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def cumplir_anios(self):
        self.edad += 1

class Maestro(Persona):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)
        self.asignatura = []
    
    def agregar_asignatura(self, asignatura):
        self.asignatura.append(asignatura)

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)
        self.clase = []
    
    def agregar_clase(self, clase):
        self.clase.append(clase)

class Universitario(Estudiante):
    def __init__(self, nombre, edad, genero, universidad):
        super().__init__(nombre, edad, genero)
        self.universidad = universidad
