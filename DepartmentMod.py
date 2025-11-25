from AddressMod import Address
class Department:
    def __init__(self,did,dname,address):
        self.did=did
        self.dname=dname
        self.address=address

    def __str__(self):
        return f"""\n Department DID: {self.did} Department Name: {self.dname} {self.address}"""
dept=Department(10, "IT",Address("street no-7", "noida", "up","343434"))