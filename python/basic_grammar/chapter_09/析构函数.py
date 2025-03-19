"""
__function__ 魔法方法，通常用来做属性初始化等
"""


class Cat:
    # 内存回收时调用的方法
    def __init__(self):
        print("Cat init")

    def __del__(self):
        print("【析构函数】Cat has been del")

    # toString()方法,需要返回个字符串
    def __str__(self):
        return str(id(self))


cat = Cat()
print(cat)
del cat
