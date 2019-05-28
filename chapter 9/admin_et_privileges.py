from user_seulement import User


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
