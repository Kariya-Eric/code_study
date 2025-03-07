"""
字典:map
dic={name:'zs',age:'19'}
"""

dict = {"name": 'zs', "age": 10}
print(type(dict))

# 字典的增加,无则添加，有则覆盖
dict["id"] = "340101"
print(dict)
dict["id"] = "340502"
print(dict)

# 删除字段
del dict["id"]
print(dict)
# 清空字典
# dict.clear()

# 查找,不存在则会报错
print(dict["name"])
# 查看字典的key和value和entrylist
print(dict.keys())
print(dict.values())
print(dict.items())

for item in dict.items():
    print(item[0], ":", item[1])
