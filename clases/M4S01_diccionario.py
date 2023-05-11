# avion = {
#     "modelo": "Boeing 747",
#     "anio": 2010,
#     "precio": 1000000.0,
#     "horarios": ["02:20", "10:40", "19:00"],
#     "caracteristicas": {
#         "longitud": 232.8,
#         "envergadura": 64.4,
#         "altura": 19.4
#     },
#     "disponible": True
# }

# print(f'Modelo: {avion["modelo"]}')
# print(f'Año: {avion["anio"]}')
# print('Horarios: ')
# for horario in avion["horarios"]:
#     print(horario)

# avion["anio"] = 2014
# avion["disponible"] = False
# avion["horarios"].append("21:30")

# print('\nHorarios Actualizados: ')
# for horario in avion["horarios"]:
#     print(horario)


dieta = {
    "menu60": {"tipo": "carbohidratos", "cantidad_comidas": 5, "comidas": {"Desayuno": "Tazón de avena con plátano, nueces y miel.",
                                                                           "Merienda matutina": "Batido de frutas y yogur griego.",
                                                                           "Almuerzo:": "Sándwich de pollo y aguacate en pan integral.",
                                                                           "Merienda vespertina": "Palitos de zanahoria y hummus.",
                                                                           "Cena": "Pasta con salsa de tomate, espinacas y albóndigas de carne."}},
    "menu70": {"tipo": "proteinas", "cantidad_comidas": 5, "comidas": {"Desayuno": "Tortilla de claras de huevo con espinacas y queso bajo en grasas.",
                                                                       "Almuerzo": "Ensalada de pollo a la parrilla con lechuga, aguacate y nueces.",
                                                                       "Merienda": "Batido de proteína de suero de leche con plátano y mantequilla de maní.",
                                                                       "Cena": "Salmón a la parrilla con verduras salteadas y quinoa."}},
    "menu80": {"tipo": "fibras", "cantidad_comidas": 3, "comidas": {"Desayuno": "Tostadas de aguacate y huevo con frutas frescas.",
                                                                    "Almuerzo": "Ensalada de lentejas con zanahoria, apio, cebolla roja y vinagreta de limón.",
                                                                    "Cena": "Pollo al curry con arroz integral y verduras al vapor."}}
}

peso = int(input("Indique su peso (kg): "))

if peso >= 60 and peso <= 70:
    menu = dieta["menu60"]
elif peso > 70 and peso <= 80:
    menu = dieta["menu70"]
elif peso > 80:
    menu = dieta["menu80"]
else:
    "Ingrese un peso válido"

print(
    f"Su dieta recomendada es: Alta en {menu['tipo']}, {menu['cantidad_comidas']} comidas:\n")
print("----- Menú sugerido -----")
for key, value in menu['comidas'].items():
    print(f'{key}: {value}')
