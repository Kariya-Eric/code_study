# 数值类型
"""
    1、整形  任意大小的整数
    2、浮点型 小数类型
    3、布尔型 表示真假 固定写法True False 可以当做整形来看待，True=1,False=0
    4、complex 复数形式 z=a+bj b是虚部，j是虚数单位
    5、字符串
"""
num1 = -5
# <class 'int'>
print(type(num1))
num2 = 1.6
# <class 'float'>
print(type(num2))
flag = True
# <class 'bool'> 2
print(type(flag), flag + 1)
num3 = 1 + 2j
# <class 'complex'>
print(type(num3))
str1 = "hello world"
# <class 'str'>
print(type(str1), str1)
str2 = 'hello world'
print(type(str2), str2)
str3 = """
Hello
World
"""
print(type(str3), str3)
