# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

"""
Series数据对象的生成
Series生成方法: s = pd.Series(data, index=index)
Series数据类型: list, ndarray, 字典， 常量
"""
# s = pd.Series([-1, -4, -5, -3, -8], index=['a', 'b', 'c', 'd', 'e'],
#               dtype='int8')
# print(s)

# ndarry 数据类型创建Series对象
s = pd.Series(np.random.random(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

# 以字典作为数据类型创建Series对象
s = pd.Series({'a': 0, 'b': 1, 'c': 2}, index=['b', 'c', 'd', 'a'])
print(s)

# 以常量值为数据类型创建Series对象
s = pd.Series(5, index=['b', 'c', 'd', 'a'])
print(s)


"""
Series数据对象访问
Series访问方法: s.values，s.index，索引访问，切片访问
"""
s = pd.Series({'a': 0, 'b': 1, 'c': 2}, index=['b', 'c', 'd', 'a'])
print(s.index)
print(s.values)
print(s['a'])
print(s[['a', 'b']])
print(s[:2])


"""
DataFrame数据对象的生成
- DataFrame生成方法: df = pd.DataFrame(data, index=index, columns=columns)
- DataFrame数据类型：列表组成的字典、嵌套列表、Series组成的字典、字典组成的字典、二维ndarray等
"""
# 列表组成的字典形式创建
df = pd.DataFrame({'one': [1., 2., 3., 5], 'two': [1., 2., 3., 4.]}, index=['a', 'b', 'c', 'd'])
print(df)

# 以嵌套列表形式创建
df = pd.DataFrame([[1., 2., 3., 5], [1., 2., 3., 4]], index=['a', 'b'], columns=['one', 'two', 'three',  'four'])
print(df)

# 以二维ndarray创建
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2, 'hello'), (2, 3, 'world')]
print(data)
print(pd.DataFrame(data, index=['one', 'two']))

# Series组成的字典形式创建
data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
print(pd.DataFrame(data))

# 字典的列表形式创建
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data))

# 以字典的字典形式创建
df = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                   ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                   ('a', 'c'): {('A', 'B'): 5, ('A', 'B'): 6},
                   ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                   ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
print(df)

"""
DataFrame数据对象的访问
DataFrame访问方法: df.index, df.columns, df.values, df.loc, df.iloc, df.ix
"""
data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)

print(df.index)
print(df.columns)
print(df.values)
print(df['one'])  # 访问列
print(df[0:1])  # 访问行

print(df.loc[:, ['one', 'two']])  # 行标签，列标签
print(df.loc[['a', 'b'], ['one', 'two']])  # loc通过标签

print(df.iloc[0: 2, 0: 1])   # 访问前两行第一列的元素
print(df.iloc[[0, 2], [0, 1]])   # 访问第0行，第2行，第0列，第1列的元素

print(df.ix['a', ['one', 'two']])
print(df.ix['a', [0, 1]])
print(df.ix[['a', 'b'], [0, 1]])
print(df.ix[[0, 1], [0, 1]])
