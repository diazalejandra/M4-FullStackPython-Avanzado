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
