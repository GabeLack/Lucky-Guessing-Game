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

        today = datetime.datetime.now()
        # Calculate the difference in years
        age = today.year - birthdate_datetime.year
        # Check if the player hasn't had their birthday yet this year
        if (today.month, today.day) < (birthdate_datetime.month, birthdate_datetime.day):
            age -= 1
 
        if age >= 18:
            self.birthdate = birthdate_datetime
            self.age = age
            return self.birthdate, self.age
        return None
