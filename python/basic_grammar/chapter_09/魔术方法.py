# 类的注释
class Test:
    """类的初始化方法"""

    def __init__(self):
        pass

    # __call__ 允许类能像实例方法去调用
    def __call__(self, *args, **kwargs):
        print("call")


# ['__class__', '__d    elattr__', '__dict__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# print(dir(Test))

print(Test.__doc__)

t1 = Test()
# __call__语句调用
t1()

# __dict__查看类和对象中的属性
print(Test.__dict__)
# 实例对象中包含的属性和值
print(t1.__dict__)


class Human:
    """
    __str__打印实例对象，返回自定义字符串
    __repr__输出给程序Debug看
    """

    def __repr__(self):
        return "hello world"

    def __str__(self):
        return "str..."


h1 = Human()
print(h1)

"""
索引相关模式方法
getitem() setitem() delitem()
"""


class Student:
    def __getitem__(self, item):
        print("getitem", item)

    def __setitem__(self, item, value):
        print("setitem", item, value)

    def __delitem__(self, key):
        print("delitem", key)


s1 = Student()
res = s1['name']  # 自动触发__getitem__

s1['name'] = "zhangsan"
del s1['name']

# 以下不触发
s1.name = 'lisi'
print("##", s1.name)
del s1.name
