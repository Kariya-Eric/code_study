# 变量：计算器中储存空间，用于保存数据
# 格式： 变量名 = 值
# 其中 = 为赋值运算符

# coke_price对应为变量名
coke_price = 3.0
icecream_price = 10.0

total_price = coke_price + icecream_price

# 打印变量的值，变量未被赋值则报命名错误
print(total_price)

# 同一个变量可以被反复赋值，变量数据类型不相同也可以
coke_price = 3.5

# 标识符规定
"""
    只能由字母数字下划线组成，不能以数字开头
    python3版本支持中文命名，但是不推荐
    不能是关键字（python中已使用的标识符）
    严格区分大小写
"""

# 标识符惯例
"""
    见名知意
    下划线命名法 user_name
    小驼峰命名法 userName
    大驼峰命名法 UserName
"""
