# 作用域演示

def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print("After local assignment: {}".format(spam))
    do_nonlocal()
    print("After nonlocal assignment: {}".format(spam))
    do_global()
    print("After global assignment: {}".format(spam))


scope_test()
print("After invoke assignment: {}".format(spam))


# 类的定义
class ClassName:
    pass


class MyClass:
    """我的第一个Python类"""
    i = 123

    def f(self):
        return "Hello Python Class"

    def __init__(self):
        self.data = [1, 2]


print(MyClass.i)
print(MyClass().f())
print(MyClass.__doc__)
x = MyClass()
x.data = [1, 2, 3, 4, 5]
print(x.data)
print(x.f())


class Dog:
    tricks = []  # 公用同一作用域

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('a')
e.add_trick('b')

print(d.tricks)
print(e.tricks)


