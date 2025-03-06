list1 = ["a", "b", "c", 1, 2, 3, 4.0, 5.0]

# 列表的遍历
for i in list1:
    print(i)

i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# 列表的添加
list2 = ["python", "java", "c++"]
# ['a', 'b', 'c', 1, 2, 3, 4.0, 5.0, 'python', 'java', 'c++']
print(list1 + list2)
# 会改变原列表
list1.insert(0, list2)
# [['python', 'java', 'c++'], 'a', 'b', 'c', 1, 2, 3, 4.0, 5.0]
print(list1)
# 将元素添加到末尾,修改原列表
list1.append(list2)
print(list1)
# 将元素添加到末尾，将列表元素拆开
list1.extend(list2)
print(list1)

# 列表修改
list1[0] = "updated"
print(list1)
# 切片方式必须写入可迭代对象
list1[9:-1] = ["c++", "python", "java"]
print(list1)
list1[4:4] = ["α", "β", "θ"]
print(list1)
list1[:2:2] = ["γ"]
print(list1)

# 列表删除
# del listname 删除整个列表
# del list1
# print(list1)
# 删除列表指定位置的元素
del list1[2]
print(list1)
# 默认删除最后一个元素，可以传入index
print(list1.pop(3))
print(list1)
# 删除第一个出现的值，不存在则报错
list1.remove("c++")
print(list1)
# 清空list
list1.clear()
print(list1)

# 列表的查找
# in /not in 判断元素是否存在于列表中，返回True/False
print("python" in list2)
# 统计某个元素在列表中出现的次数
print(list2.count("python1"))
# 查找元素出现在某一个列表中的索引,元素不存在则报错
print(list2.index("java", ))
# 列表顺序倒序
list2.reverse()
print(list2)
# 排序，reverse值对应升降序，会修改list
list2.sort(reverse=True)
print(list2)
# 有返回值的排序

list1 = sorted(list2)
print(list1)

# 列表推导式 ['python', 'java']
print([i for i in list2 if len(i) > 3])
