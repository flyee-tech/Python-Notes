##################################################
# ----------- Python的基本数据类型 --------------- #
##################################################

# 数据类型：整型，浮点型，字符串, list, tuple, dict, set

a = 1  # 整型
b = 2.2  # 浮点型
c = 'abc'  # "abc" 字符串
d = [1, '1', "1", [a, b, []]]  # list
e = (a, b, c, d, [a, b])  # tuple
f = {"a": 1, "b": 2, c: 1, b: 2}  # dict
g = {"a", b, c}  # set

# 各种输出方式和和转义的示例
print(r'''one\\\t
two
three''')
print(3 > 2)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(123)
print(456.789)
print('Hello, world')
print(r'Hello, \'Adam\'')
print("r'Hello, \"Bart\"'")
print("r'''Hello,")
print('Lisa!\'\'\'')

# 获取Unicode的十进制码
print(ord('裴'))
print(ord('二'))
print(ord('龙'))
# 根据Unicode的十进制码获取字符
print(chr(20108))

# 根据Unicode的十六进制码来输出字符
print('\u88f4\u4e8c\u9f99')

# 把中文进行utf-8编码
b = "裴二龙".encode('utf-8')
print(b)

# 解码成中文
print('decode返回的结果: ' + b.decode('utf-8'))

# 计算长度
print(len(b.decode('utf-8')))

# 格式化输出
print('小明的上升百分比是%2.1f%%，很厉害！！' % 12.3333)

# list 有序的 可修改的
l1 = ["a", "b", "c", "d"]
l2 = []
l3 = ["a", 123, 1.2, l1, l2]
print(l1)
print(l1[-2])
print(l3)
l3[3][0] = "1111"
print(l3)

# tuple 有序的 指针不可修改的
t = (1, 2,)
print(t)

# 判断：只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = ()
y = ""
if x:
    print("11111111")
elif y:
    print("22222222")
else:
    print("33333333")

# input() 返回的是字符串类型
# I1 = input("输入出身年份: ")
# if int(I1) > 1990:
#     print("年轻")
# else:
#     print("老了啊")

# 循环：1. for name in names:
#      2. while <判断>:

i = 0
while i < 10:
    print(i)
    i += 1

# dict 类型
ages = {"aa": 1, "bb": 2}
print(ages)
print(ages["aa"])
print("cc" in ages)
print(ages.get("cc", -1))
ages.pop("aa")
print(ages)

# set 类型 set(...) add(...) remove(...)
s = {1, 2, 3}
print(s)
s = {(1, 2, (1, 2))}
print(s)
