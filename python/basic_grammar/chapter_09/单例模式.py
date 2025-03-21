"""
使用__new__关键字实现单例模式
"""


class MyInstance:
    # 在内存中为对象分配空间，返回对象的引用，返回值会引发init方法的调用，new方法没有返回值则不会触发init方法
    def __new__(cls):
        # 创建实例时首先调用的方法
        print("__new__方法")
        # 调用父类的__new__方法
        # return super().__new__(cls)
        return object.__new__(cls)

    def __init__(self):
        print("__init__方法")

    def func(self):
        print("func方法...")


my_instance = MyInstance()
my_instance1 = MyInstance()
my_instance2 = MyInstance()
# None
print(my_instance, my_instance1, my_instance2)


class Test:
    def __new__(cls):
        print("__new__方法..")
        print("调用父类的方法创建实例对象")
        ins = super().__new__(cls)
        print("ins:", ins)
        return ins

    def __init__(self):
        print("__init__方法:", self)


t1 = Test()
