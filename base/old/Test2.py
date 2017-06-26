##################################################
# --------------- Python的函数 ----------------- #
##################################################

# 使用 def 来定义函数


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power(2, 2))
print(power(200))


# 使用可变参数来计算 a * a + b * b + c * c + ...


def calc(*numbers):
    sums = 0
    for number in numbers:
        sums += number * number
    return sums


print(calc())
print(calc(3, 4, 5))
l1 = [1, 2, 3]
print(calc(*l1))


# 使用关键字参数 **args > dict  关键字参数
#              a, b, *, c, d  命名关键字参数（c和d）
#              *args > tuple  可变参数
# 组合使用时参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person("zs", 12)
person("ls", 13, address="beijing")


def person1(name, age, *, address1, address2, address3):
    print('name:', name, 'age:', age, 'other:', address1, address2, address3)


person1(1, 13, address1="beijing", address2="beijing", address3="beijing")


def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


person2('ww', 15, 16, 17, 1, 2, 3, 4, 5, city='shanghai', job='program')


# 递归函数 (缺点：过深的调用会导致栈溢出)


def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact1(10))
