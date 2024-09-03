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
        birthdate_datetime = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
        age = datetime.datetime.now().year - birthdate_datetime.year
        if age > 18:
            print("Valid")
            self.birthdate = birthdate_datetime
            self.age = age
        else:
            print("Invalid birth date, or younger than 18")
