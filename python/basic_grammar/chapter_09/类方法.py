class Test:
    __name = "zhangsan"
    num = 20

    @classmethod
    def static_method(cls):
        # 访问私有属性，使用到类
        print('static_method', cls, cls.__name)

    def test_method(self):
        print('test_method')

    @classmethod
    def set_num(cls):
        cls.num = 10

    @classmethod
    def get_num(cls):
        print(cls.num)


# Test.static_method()
# print(Test.num)
t = Test()
t.get_num()
Test.get_num()
t.set_num()
t1 = Test()
t1.get_num()
t.get_num()


class Test1:
    def instance_method(self):
        print("这是实例方法")

    @classmethod
    def class_method(cls):
        print("这是类方法", cls)

    @staticmethod
    def static_method():
        print("这是静态方法")

    def func():
        print("这是func方法,不带参数的方法")


test1 = Test1()
test1.instance_method()
# 类无法直接访问实力方法，需要传入实例参数，
Test1.instance_method(test1)
Test1.instance_method(Test1)
# 类对象和实例对象都可以访问类方法
test1.class_method()
Test1.class_method()
# 类对象和实例对象可以访问静态方法
test1.static_method()
Test1.static_method()
# TypeError: Test1.func() takes 0 positional arguments but 1 was given
# 实例对象调用午餐方法时会默认将对象本身作为参数传入函数
# test1.func()
Test1.func()
