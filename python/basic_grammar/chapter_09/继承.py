"""
子类无法继承父类的私有属性和方法
"""


class Person:
    def sing(self):
        print("singing...")

    def dance(self):
        print("dancing")


p = Person()
p.sing()
p.dance()


class Man(Person):
    pass


m = Man()
m.sing()
m.dance()


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Black(Dog):
    def sleep(self):
        print(f"{self.name} is sleeping")


b = Black("小黑")
b.sleep()
b.eat()
b.bark()

"""
重写
"""


class Cat(Animal):
    def eat(self):
        # 对父类的扩展
        # Animal.eat(self)
        # super().eat()
        print(f"{self.name} is eating fish")


c = Cat("mimi")
c.eat()


# d = Dog("wangcai")
# d.eat()

class A:
    def __init__(self):
        print("A init")


class A1(A):
    def __init__(self):
        super().__init__()
        print("A1 init")


class A2(A):
    pass


class A3(A):
    def __init__(self):
        print("A3 init")


class A11(A1):
    def __init__(self):
        print("A11 init")


# a1 = A1()
# a2 = A2()
# a3 = A3()

a11 = A11()


class A12(A2):
    # def __init__(self):
    #     print("A12 init")
    pass


a12 = A12()


class B:
    def __init__(self):
        print("B init...")
        self.num1 = '100'
        self._num2 = '200'
        self.__num3 = '300'

    def __str__(self):
        return self.num1 + "," + self._num2 + "," + self.__num3

    def __private_method(self):
        print("private method")

    # 间接访问私有方法
    def public_method(self):
        self.__private_method()
        print("public method")


# 子类无法继承父类的私有属性和方法
class B1(B):
    pass


b1 = B1()
print(b1, b1.num1, b1._num2, b1._B__num3)

b1.public_method()

# 多继承
"""
不同父类中存在同名方法，子类在调用时使用按照顺序，先使用自己类，然后按照继承顺序执行
"""


class C(A, B):
    pass


c = C()


class E:
    def test(self):
        print("E test...")


class D:
    def test(self):
        print("D test...")


class DE(E, D):

    def test(self):
        # 只执行D
        super().test()
        print("DE test...")


de = DE()
de.test()
