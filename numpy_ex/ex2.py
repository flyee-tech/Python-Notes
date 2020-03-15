import numpy as np

"""
ndarray数组的创建方法
"""

# 1. 从Python数据类型创建，具体类型根据Python基本类型来确定
# 列表
x = np.array([0, 1, 2, 3])
print(x)
# 元组
x = np.array((0, 1, 2, 3))
print(x)
# 混合
x = np.array([
    [1, 2],
    [9, 8],
    (0.1, 0.2)
])
print(x)
# 2. 使用NumPy中提供的函数来创建
# np.arange(n)
# np.ones(shape) 根据形状来生成
# np.zeros(shape)
# np.full(shape, val)
# np.eye(n) 正方形 n*n 矩阵，对角线为1，其他地方为0
