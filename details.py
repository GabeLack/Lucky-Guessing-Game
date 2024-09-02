import datetime

class Details():
    def __init__(self) -> None:
        """Initialize an instance of the Details class."""
        self.name = None
        self.birthdate = None
        self.age = None

    def in_name(self, name):
        """Input and validate the player's name."""
        if name.replace(' ', '').isalpha():
            self.name = ' '.join(name.split()).lower().title()
            print("Valid")
        else:
            print("Invalid name")

    def in_birth(self, birthdate):
        """Input and validate the player's birthdate, ensuring they are at least 18 years old."""
        if self.is_valid_birth(birthdate):
            if self.get_age(birthdate) >= 18:
                self.birthdate = birthdate
                self.age = self.get_age(birthdate)
                print("Valid")
            else:
                print("Too young")
        else:
            print("Invalid birth date, or before 1991")

    def is_valid_birth(self, input_birth):
        """Check if the provided birthdate is in the correct format and within a valid range."""
        year = int(input_birth[0:4])
        month = int(input_birth[4:6])
        day = int(input_birth[6:8])

        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return (len(input_birth) == 8
                and input_birth.isnumeric()
                and year > 1950
                and 1 <= month <= 12
                and 1 <= day <= days_per_month[month - 1])

    def get_age(self, input_birth):
        """Calculate the player's age based on their birthdate."""
        current_time = datetime.datetime.now()
        age_year = current_time.year - int(input_birth[0:4])
        return age_year