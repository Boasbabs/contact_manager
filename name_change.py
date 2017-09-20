




# Using Private

class Person:
    def __init__(self, name, gender):
        if (name == "Francis"):
            raise  ValueError("What kind of horrible parent would name their child Francis?")
        else:
            self.__name = name
            self.__gender = gender

    def __repr__(self):
        return "This person is a {} named {}".format(self.__gender, self.__name)


total_not_francis = Person("Frank", "M")
total_not_francis.__repr__
print(total_not_francis.__dict__)