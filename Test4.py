##################################################
# ----------- Python的IO --------------- #
##################################################
from io import StringIO
import os
import pickle

# f = None
# try:
#     f = open("/Users/elong/test.txt", 'r', encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# # 可以这样简写,自动关闭流
# with open("/Users/elong/test.txt", 'w', encoding='utf-8') as f:
#     f.write("你好")
# with open("/Users/elong/test.txt", 'r', encoding='utf-8') as f:
#     print(f.read())
#
# # 使用rb来读取二进制文件
# with open("/Users/elong/Pictures/bc4202f7905298223f6ce046d6ca7bcb0b46d4be.jpg", 'rb') as f:
#     print(f.read())

f = StringIO()
print(f.write("hello"))
print(f.write(' '))
print(f.write('world'))
print(f.getvalue())

print(os.name)
print(os.path.abspath('.'))
print("#########################")


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " " + str(self.age)


s = Student('张三', 1)
# print(pickle.dumps(s))
f = open('abc.txt', 'wb')
pickle.dump(s, f)
f.close()

f = open('abc.txt', 'rb')
b = pickle.load(f)
print(b)
f.close()

print("=========================")

print("cpu id:%s start running" % os.getpid())
pid = os.fork()
if pid == 0:
    print("这个是子进程啊 我的id是 %s 我的爸爸的id是 %s" % (os.getpid(), os.getppid()))
else:
    print("这个是父进程啊 我的id是 %s 我创建的子进程id是 %s" % (os.getpid(), pid))

