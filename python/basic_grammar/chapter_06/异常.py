# NameError: name 'name' is not defined
# print(name)
"""
try:
    可能引发异常现象的代码
        #不确定是否能够正常执行的代码
except 异常类型:
    发生异常时执行的代码
"""

try:
    print(1 / 0)
except Exception as e:
    # 发生了异常:division by zero
    print("发生了异常:{}".format(e))