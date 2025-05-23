count = 0
while count < 10:
    print("Hello World")
    count += 1

"""
循环计算0-100的和
"""
sum = 0
i = 0
while i <= 100:
    sum += i
    i += 1
print("0 - %d 的和为 %d" % (i - 1, sum))

"""
循环计算0-100之间偶数的和 
"""
sum_even = 0
i_even = 0
while i_even <= 100:
    if i_even % 2 == 0:
        sum_even += i_even
    i_even += 2

print("0 - %d 之间所有偶数的和为 %d" % (i_even - 2, sum_even))

"""
连续输出5行*
"""
count_stars = 0
while count_stars < 5:
    count_stars += 1
    print("*" * count_stars)

"""
不试用字符串乘法方式
"""
count_stars_i = 0
while count_stars_i < 5:
    count_stars_i += 1
    count_stars_j = 0
    while count_stars_j < count_stars_i:
        print("*", end="")
        count_stars_j += 1
    print("")

"""
打印99乘法表
"""
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (row, col, row * col), end=" ")
        col += 1
    row += 1
    print()
