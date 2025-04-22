# 数值类型
num1 = 10  # 十进制
num2 = 0b101010  # 二进制
num3 = 0o101010  # 八进制
num4 = 0x101010  # 十六进制
print(num1, num2, num3, num4)

# 整型
num5 = 10
# 浮点型
num6 = 10.0
# 科学计数法，浮点型
num7 = 1.99E12123
print(num7, type(num7))
# 复数,j,<class 'complex'>
num8 = 123 + 456j
print(num8, type(num8))

# 字符串类型
"""
转义字符：\n,\t \"
"""
str1 = "Hello Python"
print(str1[2:5:])

# 字符串常见操作
# 字符串拼接
print("Hello" + "World")
# 字符串复制
print("Hello" * 5)

# 布尔类型 True/False
# 非0的整数，非空字符串的布尔值均为True
# 空序列，空字符串，空元组，字典，集合均为False
# 自定义对象的实例，该对象的__bool__()方法范围False或者__len__()方法返回0
print(bool(10), bool(0), bool(""), bool(False), bool(0.0), bool(None))
# 数据类型转换:显式转换，隐式转换
num9 = 3.69
# 强制类型转换会自动去除掉小数部分
print(int(num9))
