"""
    内置名称空间：Python解释器启动是加载名称空间,首先被加载
    全局名称空间：随着所在执行文件产生，执行结束后回收，第二个被加载
    局部名称空间：随着函数的调用产生，调用结束后回收，如函数参数，函数内定义的变量

    不同的命名空间中可以使用相同的变量名

    python查找变量的顺序：
        局部变量 -> 全局变量 -> 内置变量
"""

"""
变量作用域：
    局部变量：函数内部，不同函数可以定义相同的局部变量
    全局变量：定义在python文件中，可以在整个python文件中使用
"""
# 作用范围为整个python文件中
name = "global_name"


def func_():
    print("函数直接引用全局变量:{}".format(name))


def func_a():
    # 与全局变量同名的局部变量
    name = "func_a"
    print(name)


def func_b():
    # 与全局变量同名的局部变量
    name = "func_b"
    print(name)


def func_c():
    print(name)


def func_d():
    # 将函数内部的变量生命为全局变量
    global global_var
    global_var = "global"
    print(global_var)


def func_e():
    # 需要将name声明为全局变量，否则会报错
    global name
    print(name)
    name = "updated_name"
    print(name)


func_()
func_a()
func_b()
func_c()
func_d()
print("global_var:{}".format(global_var))
func_e()

# 可变类型对象
list = [1, 2, 3, 4]


def update_list_a():
    print(list)
    # list地址未发生变化，不需要声明即可修改
    list[1] = "3"
    print(list)


update_list_a()

""" 
    nonlocal不能修改全局变量
    在局部作用域中，对父级作用域变量进行引用和修改，并且引用的那层
"""


def outer():
    name = "outer"

    def inner_1():
        nonlocal name
        name = "inner_1"

        def inner_2():
            nonlocal name
            name = "inner_2"

        inner_2()
        print("inner_1:{}".format(name))

    inner_1()

    print("outer:{}".format(name))


outer()

"""
匿名函数
函数名 = lambda 形参: 返回值
"""
add = lambda x=1, y=1: print(x + y)

add()

minus = lambda x, y: x - y

print(minus(3, 1))

# 获取字符串中索引为0和2的字符

str = "hello world"

get_str = lambda s: (s[0], s[1])

print(get_str(str))

# 比较两个数字的大小
num1, num2 = 60, 30

compare = lambda x, y: x if x > y else y
print(compare(num1, num2))
