"""
本质是一个闭包函数，
为已存在的对象增加功能
"""


def fn1(*args):
    print("核心业务函数..", args)


"""
标准装饰器模板
"""


def decorator(func):
    def inner(*args, **kwargs):
        print("日志记录....start")
        ret = func(*args, **kwargs)
        print("日志记录....end")
        return ret

    return inner


decorator(fn1)(1, 2, 3)

"""
装饰器语法糖
"""


@decorator
def service(**kwargs):
    print("核心业务...", kwargs)


service(name="1", age="2")
