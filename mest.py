# this is to model MEST


class Person:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Eit(Person):

    def __init__(self, name, nationality, fun_fact):
        super().__init__(name, nationality)
        self.fun_fact = fun_fact

    def recite_fun_fact(self):
        return self.fun_fact


class Fellow(Person):

    def __init__(self, name, nationality, happiness_level=50):
        super().__init__(name, nationality)
        self.happiness_level = happiness_level

    # eat method increases happiness level
    def eat(self):
        self.happiness_level += 10

    # teach method decrease happiness level
    def teach(self):
        self.happiness_level -= 10


class School:
    # this class contains both Eits and Fellow

    def __init__(self, eit, fellow):
        self.eit = eit
        self.fellow = fellow


andrew = Fellow("Andrew", "Danish", 50)

simeon = Eit("Simeon", "Nigeria", "In love with Python, not a geek yet")