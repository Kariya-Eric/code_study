"""
查询python中的关键字
"""
import keyword

# 保留字严格区分大小写
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else','except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
print(keyword.kwlist)
"""
标识符命名规则:
 1、字符（英文，中文），下划线，数字，但是不能以数字开头
 2、不能使用python保留字
 3、严格区分大小写
 4、以下划线开头的标识符一般具有特殊含义，尽量避免使用
 5、允许使用中文作为标识符，但是不推荐
"""
"""
标识符命名规范:
1、模块名尽量短小,且全小写字母，可以使用下划线分隔多个字符
2、包名尽量短小,且使用小写字母不推荐使用下划线
3、类名推荐首字母大写（驼峰风格）
4、模块内部的类使用下划线+驼峰风格命名
5、类的属性和方法名使用小写字母,单词间使用下划线连接
6、常量命名采用大写字母可以使用下划线
7、使用单下划线看透的模块变量或函数是受保护的,不能被导入
8、使用双下划线开头的实例变量的方法是私有的
9、以双下划线开头和结尾是python的专用标识
"""
name = "kariya"
age = 32
print("my name is '", name, "' and my age is '", age, "'", sep="")
