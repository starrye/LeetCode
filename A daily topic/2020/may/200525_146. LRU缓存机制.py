#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 146. LRU缓存机制.py
@time: 2020/5/25 14:19
@desc: 
"""
from typing import List

from collections import OrderedDict

"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

 

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""


class LRUCache:

    # 有序字典
    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.dict_ = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict_:
            self.dict_.move_to_end(key)
        return self.dict_.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.dict_:
            del self.dict_[key]
        self.dict_[key] = value
        if len(self.dict_) > self.maxsize:
            self.dict_.popitem(last=False)




    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.dict_ = {}
    #     self.key_list = []
    #     self.key_set = set()
    #     self.length = 0
    #
    # def get(self, key: int) -> int:
    #     if key not in self.key_list:
    #         return -1
    #     self.key_list.remove(key)
    #     self.key_list.append(key)
    #     return self.dict_[key]
    #
    # def put(self, key: int, value: int) -> None:
    #     if key in self.key_set:
    #         self.length -= 1
    #         self.key_list.remove(key)
    #     self.dict_[key] = value
    #     self.key_list.append(key)
    #     self.key_set.add(key)
    #     if self.length == self.capacity:
    #         delete_key = self.key_list.pop(0)
    #         del self.dict_[delete_key]
    #     else:
    #         self.length += 1


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put("1","1")
obj.put("2","2")
param_1 = obj.get("1")
print(param_1)
obj.put("3","3")
param_2 = obj.get("2")
print(param_2)
obj.put("4","4")
param_3 = obj.get("1")
print(param_3)
param_4 = obj.get("3")
print(param_4)
param_5 = obj.get("4")
print(param_5)
