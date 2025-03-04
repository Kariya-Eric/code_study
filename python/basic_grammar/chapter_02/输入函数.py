# 输入函数 (函数参数为输入函数的提示内容)
name = input("请输入..")
# input函数的返回值永远为字符串
print("输入的值为:", name, "类型为:", type(name))

"""
转义字符
\t 制表符 tab,通常表示四个字符，缩进
\n 换行符
\r 将当前位置移到本行开头
\\ 反斜杠符号
"""
print("hello\tworld")
print("hello\rworld")
print("hello\\world")
