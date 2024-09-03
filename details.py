import datetime
import re

class Details():
    def __init__(self) -> None:
        """Initialize an instance of the Details class."""
        self.name = None
        self.birthdate = None
        self.age = None

    def in_name(self, name):
        """Input and validate the player's name using regex."""
        if re.match(r'^[A-Za-z]+(?: [A-Za-z]+)?$', name):
            self.name = ' '.join(name.split()).lower().title()
            return self.name
        return None

    def in_birth(self, birthdate):
        """Input and validate the player's birthdate, ensuring they are at least 18 years old."""
        try:
            birthdate_datetime = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
        except ValueError:
            return
        age = datetime.datetime.now().year - birthdate_datetime.year
        if age > 18:
            self.birthdate = birthdate_datetime
            self.age = age
            return self.birthdate, self.age
        return None
