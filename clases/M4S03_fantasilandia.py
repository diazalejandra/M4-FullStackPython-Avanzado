class Ticket:
    ticket_types = [
        {
            "type": "General",
            "price": 5000,
            "correlation_number": 0
        },
        {
            "type": "VIP",
            "price": 1000,
            "correlation_number": 0
        }
    ]

    def __init__(self, sale_date, type):
        self.ticket_type = self.ticket_types[0]
        self.number = self.ticket_types[type]["correlation_number"] + 1
        self.ticket_type[type]["correlation_number"] += 1

class Token:
    paper_types = {
        "normal": 1,
        "sellado": 2
    }

    payment_types = {
        "transbank": 1,
        "PayPal": 2,
        "mercado_pago": 3,
        "cash": 4,
    }

    sales_quantity = 5

    def __init__(self):
        self.paper_type = 0
        self.payment_type = 0

class Atraction:
    people_types = {
        "child": 0,
        "mayor": 1
    }

    # Variables de Clase
    use_quantity = 0

    def __init__(self, person_type, capacity, name):
        #Variables de Instancia
        self.person_type = self.people_types[person_type]
        self.capacity = capacity
        self.name = name

carrousel = Atraction()
cars = Atraction()
sillas = Atraction()


tikect_one = Ticket()
tikect_two = Ticket()

token_one = Token()
token_two = Token()
token_three = Token()