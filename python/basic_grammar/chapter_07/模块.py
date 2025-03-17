"""
内置模块:time random os
第三方模块:
自定义模块:
1、创建模块文件
2、导入模块 import 模块名
3、使用模块
"""
import modules.my_module

modules.my_module.a()
print(modules.my_module.name)

# from 模块名 import 属性，函数
from modules.my_module import a, name

a()
print(name)

from package.my_package import a as my_package_a

# a()
my_package_a()