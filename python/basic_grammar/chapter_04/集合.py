"""
类似set,无序不重复
set=｛a,b,c...｝
set()
"""
set1 = {1, 2, 3, 1, 3, 2, 4}
print(set1)
# add追加元素必须为单一元素
set1.add(7)
# update追加元素必须为可迭代对象
set1.update("hello")
print(set1)

# 删除集合内元素
set1.remove("h")
print(set1)
# 删除不会报错
set1.discard("hello")
# 随机删除集合中的数据并返回
print(set1.pop())
set2 = {3, 4, 5, 6, 7, 10}
# 两个百战集合的并集和交际
print(set1 & set2, set1 | set2)
