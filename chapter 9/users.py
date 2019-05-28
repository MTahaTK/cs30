class User():

    def __init__(self, first, last):
        self.first = first.title()
        self.last = last.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"The person in question is named {self.first.title()} "
        f"{self.last.title()}.")

    def greet(self):
        print(f"Hello, {self.first} {self.last}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    """Represent Admin users"""

    def __init__(self, first, last):
        """Initializes Admin attributes"""
        super().__init__(first, last)
        self.privileges = Privileges([])

class Privileges():
    """Contains user privileges"""

    def __init__(self, privileges):
        """Initialzes privilege attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """Displays list of privileges available to users"""
        print("Privileges:")
        if self.privileges:
            for priv in self.privileges:
                print(f"-{priv}")
        else:
            print("This user has no privileges.")
