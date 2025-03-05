if True:
    print("条件成立")
    print("条件成立")
    print("条件成立")

print("无论什么条件均为执行，均会执行的代码")
"""
任何非零和非空对象均为真，解释为True,默认逻辑为1
数字0，空对象，None对象均为假，解释为False，默认逻辑值为0
判断的返回值为True或者False
"""
print(not 0)

age = int(input("请输入你的年龄..."))

if age >= 18:
    print("可以进入网吧...")
else:
    print("回家写作业...")

score = int(input("请输入你的成绩..."))
if 90 <= score <= 100:
    print("你的成绩为特优")
elif 80 <= score < 90:
    print("你的成绩为优秀")
elif 70 <= score < 80:
    print("你的成绩为良好")
elif 0 <= score < 70:
    print("你的成绩为请继续努力")
else:
    print("输入的数字成绩无效")

has_ticket = True
knife_length = 50
if has_ticket:
    if 20 <= knife_length:
        print("刀长度过长,无法带上车")
    else:
        print("可以正常上车")
else:
    print("没有车票,无法上车")

"""
and 布尔与
or 布尔或
not 非
"""
x = 10
y = False
print(y and x, x and y, x or y, y or x)

age = int(input("请输入年龄"))
if age < 0 or age > 120:
    print("输入年龄非法")

python_score = int(input("请输入python成绩"))
c_score = int(input("请输入c成绩"))

if python_score >= 60 or c_score >= 60:
    print("合格")
else:
    print("不合格")

"""
三元表达式：
表达式A if 判断条件 else 表达式B
"""