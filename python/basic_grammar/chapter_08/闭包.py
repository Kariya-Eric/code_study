"""
函数内部定义的函数
闭包必须内层函数对外层函数变量的引用，非全局变量
def outer():
    sum='' #定义一个非全局变量
    def inner():
        return sum+1
    return inner()
"""


# 保存局部信息不被销毁
def outer():
    age = 17

    def inner():
        nonlocal age
        age += 1
        return age

    return inner


inner_fn = outer()
print(inner_fn())
print(inner_fn())
print(inner_fn())

sum = 17


def globaler():
    global sum
    return sum + 1


print(globaler())
print(globaler())
print(globaler())


