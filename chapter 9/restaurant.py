class Restaurant():
    """Class that assembles restaurant attributes"""

    def __init__(self, name, type,):
        """Initializes restaurant attributes"""
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f"This restaurant, named {self.name.title()},"
        f" specializes in {self.type.title()} cusine. ")

    def open(self):
        """Describes the restaurant as being open"""
        print(f"{self.name.title()} is open.")

    def set_number_served(self, number_served):
        """Sets the number of people served in the restaurant."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Increments number of people served by provided values."""
        self.number_served += additional_served
