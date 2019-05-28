# 9-1
print("\n9-1")

import time

class Restaurant():
    """Class that assembles restaurant attributes"""

    def __init__(self, name, type,):
        """Initializes restaurant attributes"""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f"This restaurant, named {self.name.title()},"
        f" specializes in {self.type.title()} cusine. ")

    def open(self):
        """Describes the restaurant as being open"""
        print(f"{self.name.title()} is open.")

rest = Restaurant("something", "french")
rest.describe_restaurant()
rest.open()

# 9-2
print("\n9-2")

first = Restaurant("something1", "columbian")
second = Restaurant("something2", "russian")
third = Restaurant("something3", "english")

first.describe_restaurant()
second.describe_restaurant()
third.describe_restaurant()

# 9-3
print("\n9-3")

class User():

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def describe_user(self):
        print(f"The person in question is named {self.first.title()} "
        f"{self.last.title()}.")

    def greet(self):
        print(f"Hello, {self.first.title()} {self.last.title()}.")

person = User("Taha", "Khokhar")
person.describe_user()
person.greet()

# 9-4
print("\n9-4")

class Restaurant1():
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

x = Restaurant1("something", "somethingelse")

x.set_number_served(5)
print(x.number_served)
x.increment_number_served(9)
print(x.number_served)

# 9-5
print("\n9-5")

class User1():

    def __init__(self, first, last, login_attempts):
        self.first = first
        self.last = last
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"The person in question is named {self.first.title()} "
        f"{self.last.title()}.")

    def greet(self):
        print(f"Hello, {self.first.title()} {self.last.title()}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User1('taha', 'khokhar', 0)

user1.describe_user()
user1.greet()

print("\nAttempting login...")
# time.sleep(1)
user1.increment_login_attempts()
print("\nAttempting login x2...")
# time.sleep(1)
# user1.increment_login_attempts()
print("\nAttempting login x3...")
# time.sleep(1)
user1.increment_login_attempts()
print(f"\nAttempted login {user1.login_attempts} times.")
# time.sleep(2)
print("\nResetting login attempts...")
user1.reset_login_attempts()
print(f"Login attempts: {user1.login_attempts}.")

# 9-6
print("\n9-6")

class IceCreamStand(Restaurant1):
    """Assembles Ice Cream Stand data as a restaurant"""
    def __init__(self, name, type="ice cream"):
        super().__init__(name, type)
        self.flavours = []

    def show_flavours(self):
        """Makes a list of flavours and displays it"""
        print("The following flavours are available:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")

one = IceCreamStand('One Creamery')
one.flavours = ['vanilla', 'chocolate', 'mint', 'fudge', 'cotton candy']

one.describe_restaurant()
one.show_flavours()
# 9-7
print("\n9-7")

class Admin(User1):
    """Represent Admin users"""

    def __init__(self, first, last, login_attempts):
        """Initializes Admin attributes"""
        super().__init__(first, last, login_attempts)
        #self.privileges = []

        self.privileges = Privileges()

    # def show_privileges(self):
    #     """Displays list of privileges available to Admin users"""
    #     print("Privileges:")
    #     for priv in self.privileges:
    #         print(f"-{priv}")

# admin = Admin("taha", "khokhar", 0)

# admin.privileges = ['can add post', 'can edit', 'can ban user',
#                     'can edit post', 'can delete post', 'can access']
#
# admin.show_privileges()

# 9-8
print("\n9-8")

class Privileges():
    """Contains user privileges"""

    def __init__(self, privileges=[]):
        """Initialzes privilege attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """Displays list of privileges available to Admin users"""
        print("Privileges:")
        if self.privileges:
            for priv in self.privileges:
                print(f"-{priv}")
        else:
            print("This user has no privileges.")

admin2 = Admin('admin2', 'admin2', 0)

admin2.describe_user()

admin2.privileges.show_privileges()

print(f"No privileges detected for {admin2.first.title()}. Adding"
      " privileges.")

admin2_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    'can add post',
    'can edit',
    'can ban user',
    'can edit post',
    'can delete post',
    'can access'
    ]

admin2.privileges.privileges = admin2_privileges
admin2.privileges.show_privileges()

# 9-9
print("\n9-9")

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
