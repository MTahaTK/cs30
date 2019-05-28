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
