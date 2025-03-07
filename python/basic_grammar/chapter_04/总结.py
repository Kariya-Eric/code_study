"""
+ 字符串，列表元组中均为拼接
* 复制 字符串列表和元组中对应为复制
in not in 字符串，列表，元组中判断存在不存在
"""
# **********
str = "*"
print(str * 10)

list = [1, 2, 3, 4, 5, 6]
print(list * 5)

"""
公共方法：
len() 计算元素个数
del 删除元素
max() min()
range() 序列相关 'set' object cannot be interpreted as an integer
enumerate() 下标数据一一列出
"""
set1 = {1, 3, 2, 5}
# print(set1)
# del set1
# print(set1)
# print(max(set1))

for i, value in enumerate(list):
    print(i, value)

dict = {"name": 'zs', "age": 10, "gender": "female"}

for key, value in dict.items():
    print(key, value)

# 列表推导式
print([i for i in list if i % 2 == 0])
# 元组推导式返回对象地址，
tuple1 = (i for i in list if i % 2 != 0)
# <generator object <genexpr> at 0x000002E7DF21F6B0>
print(tuple(tuple1))
# 字典推导式

dict1 = {"s{}".format(i): "{}".format(i * 2) for i in range(1, 11)}
print(dict1)
