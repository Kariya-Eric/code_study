"""
class 类名(父类)：
    成员
"""


class Person(object):
    # 属性
    name = None

    # 方法
    def info(self):
        print("self:", self)


# 创建对象
# self: <__main__.Person object at 0x0000025A27329DF0>
# self: <__main__.Person object at 0x0000025A27329E20>
p1 = Person()
p1.info()
print(p1.name)


class Student(object):
    name = None

    # 构造函数
    def __init__(self, name):
        print("Student init")
        self.name = name


s1 = Student("张三")
print(s1.name)