"""
@author: KARIYA
"""
print("this is a package info")
import chapter_07.package.my_package as pac

print(type(pac))

# 定义 __all__变量
__all__ = ["pac"]
