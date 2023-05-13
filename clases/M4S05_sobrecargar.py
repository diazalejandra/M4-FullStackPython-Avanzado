class Persona:
    message_base = "Te Estoy llamando"
    def __init__(self, name):
        self.name = name

    def llamar(self):
        print(self.message_base)

    def llamar(self, medio=''):
        message = self.message_base
        if (medio != ''):
            message = f"{self.message_base} con {medio}"
        print(message)

    def llamar(self, medio='', time= ''):
        message = self.message_base
        if (medio != '' and time == ''):
            message = f"{self.message_base} con {medio}"
        if (medio != '' and time != ''):
            message = f"{self.message_base} con {medio} a las {time}"
        print(message)


juan = Persona("Juan")

juan.llamar("Telefono", '15:00 horas')