# Classes start with capital letter and are singular
# 'Innit self' gets invoked every time a new object is created & initializes the instance's attributes
# All instance methods need a self parameter
# All subclasses inherit attributes from parent class

class Band:

    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __str__(self):
        return f'This Bands name is {self.name}'

    def __repr__(self):
        return f'Band instance. Name = {self.name}'

    def play_solos(self):
        play_solo = [member.play_solo() for member in self.members]
        return play_solo


class Musician:

    def __init__(self, name):
        self.name = name


class Guitarist(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):


    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'


if __name__ == "__main__":
    pass

