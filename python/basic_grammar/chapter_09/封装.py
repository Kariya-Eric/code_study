class Student:
    name = None
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add(self):
        self.age += 1

    def __str__(self):
        return f'{self.name} is {self.age} years old'


s1 = Student('zhangsan', 17)
print(s1)
s1.add()
print(s1)


class Animal:
    # 私有属性，子类可以访问
    __name = None
    _type = None

    def __init__(self, name, type):
        print("Animal init", type, name)
        self.__name = name
        self._type = type

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # def __str__(self):
    #     return f'{self.__name}'


class Cat(Animal):
    def __str__(self):
        return f'{self.get_name()}--{self._type}'


c1 = Cat("zhangsan", 'cat')
print(c1)


class Classmate:
    name = "lucy"
    _age = 20
    __sex = "F"


pr = Classmate()
print(Classmate.name)
print(Classmate._age)
# 强行获取私有属性的方法，对象._类名__私有属性名
print(pr._Classmate__sex)
