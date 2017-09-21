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

class MoneyException(Exception):
    def __init__(self,arg):
        self.arg = arg


class Fellow(Person):
    # fixed number of Fellow to be created
    number_of_fellow = 1

    def __init__(self, name, nationality, happiness_level=50):
        super().__init__(name, nationality)
        self.happiness_level = happiness_level

        try:
            Fellow.number_of_fellow += 1
            if Fellow.number_of_fellow > 5:
                raise MoneyException(name)
        except Exception as error:
            print("We can't hire {}!".format(error))

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
francis = Fellow("Francis", "Ghanaian", 60)
kerry = Fellow("Kerry", "USA", 70 )
miishe = Fellow("Miishe", "USA", 80)
pascal = Fellow("Pascal", "Congo", 80)
todd = Fellow("Todd", "USA", 60)
edem = Fellow("Edem", "Ghana", 70)


# print(andrew.nationality)
# simeon = Person("Simeon", "Nigeria")
# print(simeon.name)