import datetime

from person import Person


class Age(Person):
    "Calculates the age of a person"

    def __init__(self, name, surname, birthdate, address, telephone, email):
        "Initiates the values for age"
        super().__init__(name, surname, birthdate, address, telephone, email)
        self.age = None
        self.age_last_recalculated = None
        self.recalculate_age()

    def recalculate_age(self):
        "Takes today's date and calculates the person's age in years"
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month,
                                 self.birthdate.day):
            age -= 1
        self.age = age
        self.age_last_recalculated = today

    def age(self):
        "Checks to make sure that the inputted birthdate is not in the future"
        if (datetime.date.today() > self.age_last_recalculated):
            self.recalculate_age()
        return self.age
