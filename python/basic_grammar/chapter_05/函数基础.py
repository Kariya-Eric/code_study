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


# 关键字参数
def divide(**kwargs):
    print(kwargs)


divide(name="zhangsan", age=18)


# 命名关键字，
def person(name, age, *, city="shanghai", job="coder"):
    print(name, age, city, job)


person("zhangsan", 18)

"""
参数的定义顺序：
必选参数（位置参数）,默认参数，可变参数，命名关键字和关键字参数
func(a,b=10,*c,d,e=10,**kwargs)
"""


def func(a, b=10, *args, c, **kwargs):
    print(a, b, args, c, kwargs)


# 1 3 (4, 5, 6, 7)
func(1, 3, 4, 5, 6, 7, c="a", name="zhangsan", age=18)
