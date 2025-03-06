a = "hello"
# <class 'bytes'> 字节流
b = b"hello"
print(type(b))

# 将a字符串进行编码 b'hello'
a1 = a.encode()
print(a1)

# 将字节流进行解码，默认编码UTF-8
print(b.decode())

str = "hello world"

"""
    str[start:end:step]
    切片不会报错
"""

# 字符串常用方法
# 查找到第一次出现的子串下标,未找到返回-1
print(str.find("l"))
# 查找第一次出现子串下标，未找到抛异常
print(str.index("lo"))
# 查找子序列在目标字符串中出现的个数
print(str.count("l"))
# 字符串替换,将目标字符串的所有字符替换为
print(str.replace("l", "a"))
# 字符串分割 ['hello', 'world'] 返回字符串集合
print(str.split(" "))
# 首字母大写
print(str.capitalize())
# 大小写,字符串每个单词的首字母大写,判断大小写是否为数字
"""
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
"""
print(str.lower(), str.upper(), str.title(), str.islower(), str.isupper(), str.isnumeric(), str.isdigit())

"""
判断字符串是不是以子串开头,以子串结尾
"""
print(str.startswith("l", 3), str.endswith("d"))

"""
字符串拼接,+号拼接
h*e*l*l*o* *w*o*r*l*d join在每个字符后都加入*
"""
print(str + " kariya", "*".join(str))

"""
删除左右空格和两端空格 lstrip,rstrip,strip 
"""
print(str.lstrip(),str.rstrip(),str.strip())