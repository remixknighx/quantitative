# -*- coding: utf-8 -*-
"""
关于collections的相关用法
https://blog.csdn.net/wangqing_12345/article/details/71159241
"""
from collections import *
from queue import Queue
import copy


"""
tuple不可变对象
1. 性能优化
2. 线程安全
3. 可以作为dict的key
4. 拆包特性
"""
def tuple_exercise():
    user_tuple = ("bobby", 39, 187)
    # 拆包
    name, age, height = user_tuple
    print(name, age, height)


"""
namedtuple创建class
节省内存，提高效率
"""
def namedtuple_exercise():
    User = namedtuple("User", ["name", "age", "height"])
    user = User(name="bobby", age=29, height=175)

    # 拆包
    name, age, height = user
    print(name, age, height)

    user2 = User(*("bobby", 29, 175))
    print(user.age, user.name, user.height)
    print(user2.age, user2.name)

    user_info_dict = user._asdict() # 转化成dict
    print(user_info_dict)


"""
*args, 不指明参数名称，参数转化成tuple
**kwargs: 指明参数，参数转化为key为参数名的dict
"""
def ask(*args, **kwargs):
    pass


"""
defaultdict使用
不需要判断是否为空再赋值
"""
def defaultdict_exercise():
    users = ["bobby1", "bobby2", "bobby1", "bobby2"]
    user_default_dict = defaultdict(int)
    for user in users:
        user_default_dict[user] += 1
    print(user_default_dict)


"""
deque使用
deque是线程安全的
list非线程安全的
"""
def deque_exercise():
    user_deque = deque(("bobby1", "bobby2"))
    user_deque1 = deque({
        "bobby3": 25,
        "bobby4": 27
    })
    use_deque_copy = copy.deepcopy(user_deque)


"""
counter统计
"""
def counter_exercise():
    user_counter = Counter(["bobby1", "bobby2", "bobby1", "bobby2"])
    print(user_counter)
    str_counter = Counter("fsadfsfg")
    str_counter.update("sdfsdfasd") # 补充字符串
    print(str_counter.most_common(2)) # 统计次数前n的字符串
    print(str_counter)


"""
OrderedDict 可排序dict
按添加顺序排序
"""
def ordered_dict():
    user_dict = OrderedDict()
    user_dict["b"] = "bobby2"
    user_dict["a"] = "bobby1"
    user_dict["c"] = "bobby3"
    print(user_dict)


"""
ChainMap
合并多个dict
"""
def chainmap_exercise():
    user_dict1 = {"a": "bobby1", "b":"bobby2"}
    user_dict2 = {"b": "bobby3", "d": "bobby4"}
    user_dict_all = ChainMap(user_dict1, user_dict2)
    print(user_dict_all)
    for k, v in user_dict_all.items():
        print(k, v)


if __name__ == '__main__':
    # tuple_exercise()
    # namedtuple_exercise()
    # defaultdict_exercise()
    chainmap_exercise()