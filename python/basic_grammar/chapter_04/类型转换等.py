age = 10
age_str = str(age)
print(age_str, type(age_str))
age_str_int = int(age_str)
print(age_str_int, type(age_str_int))
age_tuple = tuple(age_str)
print(age_tuple, type(age_tuple))
age_list = list(age_str)
print(age_list, type(age_list))
# 先使用打包
print(zip(age_str, "251"))
age_dict = dict(zip(age_str, "25"))
print(age_dict, type(age_dict))
age_float = float(age)
print(age_float, type(age_float))

age2 = 10
# 查看内存地址
print(id(age), id(age2))
import copy

list1 = [1, 2, 3, 4]
list2 = list1
list_copy = copy.copy(list1)
# copy的内存地址不同
print(id(list1), id(list_copy), id(list2))

# 不可变对象，存储空间中保存的数据内容,值不可发生变化,地址可以发生变化
# int bool float complex str tuple 更改内容会使地址发生变化

set1 = {1, 2}
print(id(set1))
set1.add(1)
print(id(set1))
