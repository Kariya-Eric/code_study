"""
文件读取 f=open("文件名“,"访问方式")
f。close() 文件关闭，返回true表示已关闭
mode="r" read
mode="w" write
mode="a" 追加append
mode="rb" ，wb ，ap 二进制格式
r+,w+,a+,读写 rb+ wb+ ab+
"""

# f = open("./data.txt", mode="r", encoding="UTF-8")
# content = f.read()
# print(content)
#
# f.close()
# try:
#     f = open("./log.txt", mode="a", encoding="UTF-8")
#     f.write("床前明月光，\n")
#     f.write("疑似地上霜。\n")
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# 二进制文件写入
# f = open("./data.txt", mode="rb")
#
# content = f.read()
# print(content.decode("utf-8"))
#
# f.close()

"""
with关键字，等同于try except finally
"""
# with open("./data.txt", mode="rb") as f:
#     print(f.read().decode("utf-8"))
#
# # True，已关闭
# print(f.closed)

with open("./data.txt", mode="r", encoding="utf-8") as f:
    print("read:", f.read(10))

    position = f.tell()
    print("position:", position)
    #     吧指针位置重新定位到初始位置，第一个0是偏移量，第二个0是指针位置,0开始，1对应当前位置，2对应结尾
    position = f.seek(0, 1)
    print("read:", f.read(10))
