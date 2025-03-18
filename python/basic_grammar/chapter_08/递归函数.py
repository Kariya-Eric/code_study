"""
1-100的求和
"""
sum = 0
for i in range(101):
    sum += i
print(sum)


# 使用递归计算1-100的求和
def sum(num):
    if num == 1:
        return 1
    return num + sum(num - 1)


print(sum(100))


# 斐波那契数列 1，1，2，3，5，8，13
def fibonacci(num):
    if num == 1 or num == 2: return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(3), fibonacci(4), fibonacci(5), fibonacci(6), fibonacci(7), fibonacci(8), fibonacci(9))


# 阶乘
def jiecheng(num):
    if num == 1: return 1
    return jiecheng(num - 1) * num


print(jiecheng(5), jiecheng(4), jiecheng(3))

