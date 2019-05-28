class Person():
    "Information about a person and initiates values"

    def __init__(self, name, surname, birthdate, address, telephone, email):
        """Initializes information about person"""
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
