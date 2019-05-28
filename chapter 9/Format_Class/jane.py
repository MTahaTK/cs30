import datetime

from age import Age

jane = Age(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12),  # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

jane.fullname = jane.name + " " + jane.surname
print(jane.name + "'s birthday is " + str(jane.birthdate))
print(jane.fullname + " is " + str(jane.age) + " years old.")
