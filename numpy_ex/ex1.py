import numpy as np


def pySum():
    """
    用普通的方式来计算 a² + b³ 的和，a和b都是数组
    """
    a = [0, 1, 2, 3, 4]
    b = [9, 8, 7, 6, 5]
    c = []

    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)

    return c


def npSum():
    """
    用 numpy 的方式来实现是什么效果
    """
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    c = a ** 2 + b ** 3
    return c


if __name__ == '__main__':
    print(pySum())
    print(npSum())
