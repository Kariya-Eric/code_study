"""
python内置函数
"""
print("屏幕输出")
# 将可迭代序列转换为对应的数据类型
print(set())
print(list())
print(tuple())

# abs返回绝对值
print(abs(-32231))
# 求和
print(sum([1, 2, 3]))
# zip()拉链函数,将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的内容
a = {1, 2, 3, 4}
b = {4, 5, 6}
print(list(zip(a, b)))

# map() 映射函数 map(function,iterable) 映射函数
list1 = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * x, list1)))

# reduce() 函数 对参数序列中的参数通过计算使得项不断减少 reduce(函数名,可迭代对象)
list2 = [1, 2, 3, 4, 5]
from functools import reduce

print(reduce(lambda x, y: x + y, list2))

# enumerate美剧 用于将一个可遍历的数据对象组合为一个索引序列，同事列出数据和数据下标
li = ["a", "b", "c", "d", "e"]
for i, j in enumerate(li):
    print(i, j)

print(dict(enumerate(li)))

"""
拆包：对于函数中多个返回数据，去掉元组，列表或者字典，直接获取里面的数据
"""
list3 = [1, 2, 3, 4]
a, *b = list3
print(a, b)
str = "hello world"
a, *b = str
print(a, b)
a, *b, c, d, e = str
print(a, b, c, d, e)

dict1 = {"name": "zhangsan", "age": 18, "gender": "male"}
a, *b, c = dict1
# name ['age'] gender 解构字段只返回key
print(a, b, c)
