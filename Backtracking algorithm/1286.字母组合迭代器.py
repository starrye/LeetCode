#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1286.字母组合迭代器.py
@time: 2020/4/25 15:24
@desc: 
"""
"""
请你设计一个迭代器类，包括以下内容：
一个构造函数，输入参数包括：一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLength 。
函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。
函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 True；否则，返回 False。
 
示例：

CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator

iterator.next(); // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "bc"
iterator.hasNext(); // 返回 false
 

提示：

1 <= combinationLength <= characters.length <= 15
每组测试数据最多包含 10^4 次函数调用。
题目保证每次调用函数 next 时都存在下一个字母组合。
"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.result = []
        self.count = 0
        self.get_letters("", self.characters)

    def get_letters(self, tmp_str, selectable_str):
        if len(tmp_str) == self.combinationLength:
            self.result.append(tmp_str[:])
            return
        selectable_str_tmp = selectable_str
        # 在for循环内 应该定义临时列表(选择列表) 对临时列表进行[1:]操作 然后以可选列表进行下一次递归
        for i in selectable_str:
            if i in tmp_str:
                continue
            selectable_str_tmp = selectable_str_tmp[1:]
            # 选择
            tmp_str += i
            self.get_letters(tmp_str, selectable_str_tmp)
            # 撤销选择
            tmp_str = tmp_str[:-1]

    def next(self) -> str:
        self.count += 1
        return self.result[self.count - 1]

    def hasNext(self) -> bool:
        return len(self.result) > self.count


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
param_1 = obj.next()
param_2 = obj.hasNext()
obj.next()
obj.hasNext()
obj.next()
obj.hasNext()
