# -*- coding: utf-8 -*-

import numpy as np

"""
 Array数组
 - rank 数组维度
 - zeros 创建全部为0的数组
 - ones 创建全部为1的数组
 - full 创建全部为相同值的数组
 - eye 创建单位矩阵
 - random.random 创建随机矩阵
"""
# a = np.array([1, 2, 3])
# print(type(a))   # 数据类型 numpy.ndarray
# print(a.ran)
# print(a.shape)   # 数据大小
# a = a.reshape((1, -1))     # 1表示整个数组只有一行，-1 占位符 代表3
#
# b = np.zeros((3, 3))
# print(b)
#
# c = np.ones((3, 3))
# print(c)
#
# d = np.full((3, 3), 2)
# print(d)
#
# e = np.eye(4)
# print(e)
#
# f = np.random.random((3, 4))
# print(f)

"""
数组索引indexing

- arange 产生指定范围内的数组
"""
# a = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])
# print(a[1:, 1:3])
# print(a[1, 1:3])
# 为每行第二列元素加10
# a[0:3, 1] += 10
# a[[0, 1, 2], 1] += 10
# a[[0, 1, 2], [1, 1, 1]] += 10
# a[np.arange(3), [1, 1, 1]] += 10
# a[np.arange(3), 1] += 10
# print(a)

# 获取大于10的元素
# result_index = a > 10
# print(a[result_index])


"""
元素的数据类型
"""
# a = np.array([1, 2])
# print(a.dtype)
#
# a = np.array([1.3, 2])
# print(a.dtype)
#
# 指定数据类型，np.int64向下取整
# a = np.array([1.3, 2.6], dtype=np.float64)
# print(a)

"""
数学运算与常用函数
"""
# a = np.array([[1, 2],
#              [3, 4]])
# b = np.array([[5, 6],
#              [7, 8]])
#
# # 加法
# print(a + b)
# print(np.add(a, b))
#
# # 减法
# print(a - b)
# print(np.subtract(a, b))
#
# # 乘法
# print(a * b)
# print(np.multiply(a, b))
#
# # 除法
# print(a / b)
# print(np.divide(a, b))
#
# # 开方
# print(np.sqrt(a))
#
# # 矩阵乘法
# c = np.array([[1, 2, 3],
#               [3, 5, 7]])
# print(a.dot(c))
# print(np.dot(a, b))
#
# # sum函数
# print(np.sum(a))  # 所有元素求和
# print(np.sum(a, axis=0))  # 数组中每一列进行求和
# print(np.sum(a, axis=1))  # 数组中每一行进行求和
#
# # mean函数
# print(np.mean(a))
# print(np.mean(a, axis=0))  # 数组中每一列求平均值
# print(np.mean(a, axis=1))  # 数组中每一行求平均值
#
# # uniform 随机数
# print(np.random.uniform(3, 4))  # 生成3～4之间的随机数值
#
# # tile 将数组作为元素重复指定的次数
# print(np.tile(a, (1, 2)))
# print(np.tile(a, (2, 1)))
#
# # argsort 将数组中的元素进行排序
# a = np.array([[5, 7, 3, 8],
#               [11, 64, 4, 34]])
# print(a.argsort())  # 每一行进行排序
#
# # 矩阵转置
# a = np.array([[5, 7, 3, 8],
#               [11, 64, 4, 34]])
# print('--------------------')
# print(a.T)
# print(np.transpose(a))

"""
广播
"""
# a = np.array([[1, 2, 3],
#               [2, 3, 4],
#               [45, 34, 2]])
# b = np.array([5, 6, 8])
# # 将a的每一行与b相加
# print(a + np.tile(b, (3, 1)))
# print(a + b)
