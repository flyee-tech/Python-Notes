##################################################
# --------------- Python高级特性 ----------------- #
##################################################
import os

# 切片 > ist、String 和 tuple 都可以使用[*:*:*] 来进行切片取数据
import functools

l1 = [1, 2, 3, 4, 5, 6]
print(l1[:3])
print(l1[-3:])
print(l1[1::2])

t1 = (l1, 2, 3, 4, 5)
print(t1[:1])
print(t1[-1:])
print(t1[::3])

s1 = "peierlong"
print(s1[-4:])
print(s1[::2])

# 列表生成式
print([x * x * x for x in range(1, 11)])
print([x * x * x for x in range(1, 11) if x % 2 == 0])
print([m + n + j for m in "ABC" for n in "DEF" for j in "GHI"])
print([d for d in os.listdir('.')])
print([k + "=" + v for k, v in {"a": "A", "b": "B", "c": "C"}.items()])

# 生成器
g = (x * x * x for x in range(1, 11))
for n in g:
    print(n)


def fib(maxNum):
    n, a, b = 0, 0, 1
    while n < maxNum:
        yield b  # 使用yield来生成一个generator
        a, b = b, a + b
        n += 1
    return 'done'


for n in fib(10):
    print(n)


# 可作用于for循环的对象都是Iterable类型，凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列。

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 使用filter() 产生所有质数

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


print("------- 输出1000之内的质数 ----------")
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
print("------- 输出完毕 ----------")

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
sorted([36, 5, -12, 9, -21], key=abs)  # 绝对值处理后排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  # 忽略大小写排序


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 匿名函数 lambda

def build(x, y):
    return lambda j: (x * x + y * y) * j


f = build(1, 2)
print(f(2))


# 装饰器 decorator

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kv):
        print("call %s():" % func.__name__)
        return func(*args, **kv)

    return wrapper


@log
def now():
    print("2017-01-10")

now()
print(now.__name__)

# 偏函数

int2 = functools.partial(int, base=8)
print(int2("11"))
