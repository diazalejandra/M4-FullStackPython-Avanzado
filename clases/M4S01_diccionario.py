avion = {
    "modelo": "Boeing 747",
    "anio": 2010,
    "precio": 1000000.0,
    "horarios": ["02:20", "10:40", "19:00"],
    "caracteristicas": {
        "longitud": 232.8,
        "envergadura": 64.4,
        "altura": 19.4
    },
    "disponible": True
}

print(f'Modelo: {avion["modelo"]}')
print(f'Año: {avion["anio"]}')
print('Horarios: ')
for horario in avion["horarios"]:
    print(horario)

avion["anio"] = 2014
avion["disponible"] = False
avion["horarios"].append("21:30")

print('\nHorarios Actualizados: ')
for horario in avion["horarios"]:
    print(horario)
