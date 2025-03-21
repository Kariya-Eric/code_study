class Animal:
    def eat(self): pass


class Cat(Animal):
    def eat(self): print("cat is eating fish")


class Dog(Animal):
    def eat(self): print("dog is eating bone")


class Cow(Animal):
    def eat(self): print("cow is eating grass")


def eat(animal):
    animal.eat()


eat(Cow())
eat(Cat())
eat(Dog())
