"""
计算1-100的和
"""
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("1-100的和为:", sum)

"""
计算1-100之间偶数的累加和
"""
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 2
print("1-100之间的偶数累加和:", sum)

# 99乘法表
row = 1

while row <= 9:
    col = 1
    while col <= row:
        print("{} * {} = {}".format(col, row, row * col), end="\t")
        col += 1
    print()
    row += 1

"""
range(start,end,step)函数，左闭右开，step对应步长
"""
for i in range(0, 10, 2):
    print(i, end="\t")
