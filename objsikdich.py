# objects ko barema sikeko
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello my name is {self.name}")


kirtan = Person("Kirtan")
kirtan.talk()

bob = Person("Bob")
bob.talk()

