class Address:
    def __init__(self,street,city,state,pin):
        self.street=street
        self.city=city
        self.state=state
        self.pin=pin

    def __str__(self):
        return f"""\n Address: {self.street} {self.city} {self.state}  {self.pin}"""