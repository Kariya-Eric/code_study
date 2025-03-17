# NameError: name 'name' is not defined
# print(name)
"""
try:
    可能引发异常现象的代码
        #不确定是否能够正常执行的代码
except 异常类型:
    发生异常时执行的代码
"""

try:
    print(1 / 0)
# except非必须
except Exception as e:
    # 发生了异常:division by zero
    print("发生了异常:{}".format(e))
# else:
#     print("未发生异常才会执行的代码")
finally:
    print("最终需要执行的代码")


def func1():
    print(1 / 0)


def func2():
    func1()


try:
    func2()
except Exception as e:
    print("发生了异常", e)

"""
异常主动抛出
"""


def func3():
    # 主动抛出异常
    raise Exception("主动抛出一个异常")
    print("hello world")


try:
    func3()
except Exception as e:
    print(e)
