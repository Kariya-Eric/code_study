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


# 模块的导入也是单例模式
# __new__ 单例模式
class Test:
    __singleton_instance = None

    def __new__(cls, *args, **kwargs):
        if Test.__singleton_instance is None:
            Test.__singleton_instance = object.__new__(cls)
        return Test.__singleton_instance

    def __init__(self, name):
        print("..init", self)
        self.name = name


t1 = Test("zhangsan")
t2 = Test("lisi")
print(t1 is t2, t1.name, t2.name)


# 类方法
class Singleton2:
    __instance = None

    @classmethod
    def get_instance(cls):
        if Singleton2.__instance is None:
            Singleton2.__instance = object.__new__(cls)
        return Singleton2.__instance


s1 = Singleton2.get_instance()
s2 = Singleton2.get_instance()
print(s1, s2, s1 is s2)


# 装饰器生成单例模式
def outer(fn):
    _ins = {}

    def inner(*args, **kwargs):
        if fn not in _ins:
            _ins[fn] = fn(*args, **kwargs)
            print(fn, _ins, _ins[fn])
        return _ins[fn]

    return inner


@outer
class Singleton3:
    pass


s31 = Singleton3()
s32 = Singleton3()
print(s31 is s32)


# 使用元类实现单例模式
class Singleton4:
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 对象不存在_ins属性
        if not hasattr(cls, '_ins'):
            cls._ins = object.__new__(cls)
        return cls._ins


s41 = Singleton4("张三")
s42 = Singleton4("李四")
print(s41 is s42, s41.name, s42.name)
