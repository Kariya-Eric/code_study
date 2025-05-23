"""
与:and  并且  条件1和条件2均成立 ==> true
或:or 或者 条件1或者条件2成立 ==> true
非:not 取反
"""
age = 70
# 判断年龄是否合法:
# age > 0 and age <= 120
if 0 < age <= 120:
    print("年龄合法")
else:
    print("年龄非法")
