# 2.- se requiere realizar un programa para vender que sirva para controlar la operación diaria de un cine

# - Registrar un cine (nombre, rut y dirección)
# - Registrar las salas y sus asientos (numeración)
# - Se puedan registar la cartelera de cada día, las películas de ese día y los respectivos horarios,
#   registrar las salas de cada película
# - Colocar un valor estándar por tipo de entrada, normal o vip,
# - Poder vender la boletería de cada dia y asignar asientos por ticket,
#   verificar que el asiento escogido ya no este vendido
# - Reportar las entradas totales vendidas por cada dia
# - Reportar las entradas vendidas por cada función
# - Reportar las entradas totales vendidas por películas
# - Reportar las entradas totales vendidas por cada dia, película y funcion

# NOTA:
# Debe considerar diagramar las clases que interactuaran en el programa, así como manejar las excepciones,
# y hacer un menu de seleccion de las opciones


class Cine:
    price_ticket_type = {
        "regular": 4000,
        "vip": 7500,
    }

    def __init__(self, _name, _rut, _address):
        self.name = _name
        self.rut = _rut
        self.address = _address
        self.room = []
        self.cartelera = []
        self.ticket_vendido = []
        self.movies = []

    def total_entradas_vendidas(self, date):
        total_entradas_vendidas = 0
        for funcion in self.cartelera:
            if funcion.date == date:
                total_entradas_vendidas += funcion.getTicketVendido()
        print(
            f"Total de entradas vendidas en la fecha {date}: {total_entradas_vendidas}"
        )

    def total_entradas_funcion(self):
        for funcion in self.cartelera:
            print(
                f"Total de entradas vendidas en la funcion {funcion.name.title}: {funcion.getTicketVendido()}"
            )

    def total_entradas_peliculas(self):
        for pelicula in self.movies:
            contador = 0

            for ticket in self.ticket_vendido:
                if ticket["movie"] == pelicula.title:
                    contador += 1
            print(
                f"La cantidad de tickets vendidos para la película {pelicula.title} es : {contador}"
            )

    # - como Reportar las entradas totales vendidas por cada dia, película y funcion
    def reporte_general(self):
        dates = []
        for ticket in self.ticket_vendido:
            dates.append(ticket["date"])
        dates = list(set(dates))
        for date in dates:
            self.total_entradas_vendidas(date)
            for funcion in self.cartelera:
                if funcion.date == date:
                    print(
                        f"Total de entradas vendidas en la funcion {funcion.name.title}: {funcion.getTicketVendido()}"
                    )
            for pelicula in self.movies:
                contador = 0
                for funcion in self.cartelera:
                    if funcion.name.title == pelicula.title and funcion.date == date:
                        contador += funcion.getTicketVendido()
                if contador > 0:
                    print(
                        f"La cantidad de tickets vendidos para la película {pelicula.title} es : {contador}"
                    )

    def add_room(self, _room):
        self.room.append(_room)

    def add_movie(self, _movie):
        self.movies.append(_movie)

    def add_function(self, _function):
        self.cartelera.append(_function)

    def venderTicket(self, day, _function, _fila, _columna, type):
        for asiento in _function.room.seat:
            # print(type(asiento.column))
            if asiento.row == _fila and asiento.column == _columna:
                if asiento.vendido is True:
                    print("El asiento seleccionado esta vendido.")
                    return
                else:
                    asiento.sell()
                    _function.incrementarTicketVendido()

        self.ticket_vendido.append(
            {
                "cine": self.name,
                "movie": _function.name.title,
                "date": day,
                "time": _function.time,
                "seat": _fila + str(_columna),
                "type": type,
                "price": self.price_ticket_type[type],
            }
        )
        print("Venta exitosa: ")
        print(self.ticket_vendido[-1])

    def mostrar_venta(self):
        print(self.ticket_vendido)

    def mostrar_cartelera(self):
        return self.cartelera


class Sala:
    def __init__(self, _number, _num_fila, _asientos_por_filas, _room_type):
        self.number = _number
        self.num_fila = _num_fila
        self.asientos_por_filas = _asientos_por_filas
        self.room_type = _room_type
        self.seat = self.crear_asientos()

    def crear_asientos(self):
        seats = []
        for fila in range(97, 97 + self.num_fila):
            for numero in range(1, self.asientos_por_filas + 1):
                asiento = Seat(chr(fila), numero)
                seats.append(asiento)
        return seats


class Seat:
    def __init__(self, _row, _column):
        self.row = _row
        self.column = _column
        self.vendido = False

    # Este metodo cambia el status a False para mostrar que el ticket
    # esta vendido.

    def soldOut(self):
        return self.vendido

    # Este metodo realiza la accion de vender un ticket

    def sell(self):
        self.vendido = True

    # Se obtiene el nombre o numero de asiento

    def getName(self):
        return f"{self.row}-{self.column}"


class Ticket:
    def __init__(self, _id, _movie, _cinema, _room, _date, _time, _price, _ticket_type):
        self.id = _id
        self.movie = _movie
        self.cinema = _cinema
        self.room = _room
        self.date = _date
        self.time = _time
        self.price = _price
        self.ticket_type = _ticket_type


class Function:
    def __init__(self, _movie, _time, _date, _room):
        self.name = _movie
        self.time = _time
        self.date = _date
        self.room = _room
        self.tickets_vendidos = 0

    def getTicketVendido(self):
        return self.tickets_vendidos

    def incrementarTicketVendido(self):
        self.tickets_vendidos += 1


class Movie:
    def __init__(self, _title, _category):
        self.title = _title
        self.category = _category


cineBadPractice = Cine("CineBadPractice", "78.323.456-7", "En Algun Lugar")

sala1 = Sala("Sala1", 4, 5, "regular")
sala2 = Sala("Sala2", 4, 5, "regular")
sala3 = Sala("Sala3", 4, 5, "vip")

toyStory = Movie("Toy Story 5", "Todo Publico")
reyLeon = Movie("El Rey Leon", "Todo Publico")
spiderman = Movie("Spiderman", "Todo Publico")

cartelera10 = Function(toyStory, "10:00", "23-05-2023", sala1)
cartelera12 = Function(toyStory, "12:00", "23-05-2023", sala1)
cartelera16 = Function(toyStory, "16:00", "23-05-2023", sala1)
cartelera11 = Function(reyLeon, "11:00", "23-05-2023", sala2)
cartelera15 = Function(reyLeon, "15:00", "23-05-2023", sala2)
cartelera19 = Function(reyLeon, "19:00", "23-05-2023", sala2)
cartelera13 = Function(spiderman, "13:00", "23-05-2023", sala3)
cartelera18 = Function(spiderman, "18:00", "23-05-2023", sala3)
cartelera20 = Function(spiderman, "20:00", "23-05-2023", sala3)

cineBadPractice.add_function(cartelera10)
cineBadPractice.add_function(cartelera12)
cineBadPractice.add_function(cartelera16)
cineBadPractice.add_function(cartelera11)
cineBadPractice.add_function(cartelera15)
cineBadPractice.add_function(cartelera19)
cineBadPractice.add_function(cartelera13)
cineBadPractice.add_function(cartelera18)
cineBadPractice.add_function(cartelera20)

cineBadPractice.add_room(sala1)
cineBadPractice.add_room(sala2)
cineBadPractice.add_room(sala3)
cineBadPractice.add_movie(toyStory)
cineBadPractice.add_movie(reyLeon)
cineBadPractice.add_movie(spiderman)


cine2 = Cine("Cine2", "78.323.456-8", "En Algun Lugar2")

sala1 = Sala("Sala1", 4, 5, "regular")
sala2 = Sala("Sala2", 4, 5, "vip")

toyStory = Movie("Toy Story 5", "Todo Publico")

cartelera10 = Function(toyStory, "10:00", "23-05-2023", sala1)
cartelera11 = Function(toyStory, "11:00", "23-05-2023", sala2)

cine2.add_function(cartelera10)
cine2.add_function(cartelera11)

cine2.add_room(sala1)
cine2.add_room(sala2)
cine2.add_movie(toyStory)


# cineBadPractice.venderTicket("21-05-2023", funCartelera, "a", 4, "vip")
# cineBadPractice.venderTicket("21-05-2023", funCartelera, "a", 4, "vip")
# cineBadPractice.venderTicket("21-05-2023", funCartelera, "b", 5, "vip")
# cineBadPractice.venderTicket("21-05-2023", funCartelera, "b", 1, "regular")
# print(funCartelera.getTicketVendido())


print("*****************************************")
print(f"Bienvenido al cine {cineBadPractice.name}")
print("*****************************************")

opcion = 9
while opcion != 0:
    print("\n**** Menú ****: ")
    print("1. Ver cartelera")
    print("2. Comprar entrada")
    print("3. Reportes")
    print("0. Salir")
    opcion = int(input("\nSeleccione una opción: "))

    match opcion:
        case 1:
            print("\nCartelera del día: ")
            print("Película - Horario - Sala")
            cartelera = cineBadPractice.mostrar_cartelera()
            for funcion in cartelera:
                print(
                    f"{funcion.name.title} - {funcion.time} - {funcion.room.number}"
                )
        case 2:
            print("\nSeleccione una función: ")
            cartelera = cineBadPractice.mostrar_cartelera()
            for index, funcion in enumerate(cartelera):
                print(
                    f"{index+1}. {funcion.name.title} - {funcion.time} - {funcion.room.number}"
                )
            indice = int(input("Ingrese la función: "))
            fecha = input("Ingrese la fecha: ")
            asiento = input("Ingrese el asiento: ")
            fila = asiento[0]
            columna = int(asiento[1])
            cineBadPractice.venderTicket(
                fecha,
                cartelera[indice - 1],
                fila,
                columna,
                cartelera[indice - 1].room.room_type,
            )
        case 3:
            print("\nReportes disponibles: ")
            print("1. Total entradas vendidas")
            print("2. Total entradas por función")
            print("3. Total entradas por película")
            print("4. Reporte general")
            reporte = int(input("Seleccione la opción: "))
            match reporte:
                case 1:
                    fecha = input("Indique la fecha: ")
                    cineBadPractice.total_entradas_vendidas(fecha)
                case 2:
                    cineBadPractice.total_entradas_funcion()
                case 3:
                    cineBadPractice.total_entradas_peliculas()
                case 4:
                    cineBadPractice.reporte_general()
        case 0:
            break
        case default:
            print("Seleccione una opción válida")
