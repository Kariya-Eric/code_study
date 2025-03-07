"""
函数返回值，参数，嵌套
def 函数名()
    函数体
"""


# 函数说明文档查看help()
# help(print)

def sing():
    print("唱歌")
    # return "hello", "world"


# 函数调用,不写return等效于return None
print(sing())


def add(a, b): return a + b


print(add(1, 3))


# 默认参数
def minus(a, b=1): return a - b


print(minus(1))


# 多个参数传入，以元组方式传入,不定长参数
def multiply(*args): print(args)


multiply(1, 2, 3, 4, 5)
