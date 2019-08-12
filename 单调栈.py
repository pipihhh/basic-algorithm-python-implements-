"""
给定一个列表，返回此列表每一个元素，离该元素最近的比它小的元素（包括左和右）
"""


class MonotonousStack(object):
    def __init__(self, lst):
        self._list = lst
        self._stack = []

    def _append(self, i):
        if not self._stack:
            self._stack.append([i, ])
            return
        if self._list[self._stack[-1][-1]] == self._list[i]:
            self._stack[-1].append(i)
        else:
            self._stack.append([i, ])

    def find_min(self):
        ret = [None for _ in range(len(self._list))]
        for i in range(len(self._list)):
            if not self._stack:
                self._append(i)
                continue
            if self._stack and self._list[self._stack[-1][-1]] <= self._list[i]:
                self._append(i)
                continue
            while self._stack and self._list[self._stack[-1][-1]] > self._list[i]:
                lst = self._stack.pop()
                res = (self._stack[-1][-1], i) if self._stack else (-1, i)
                while lst:
                    ret[lst.pop()] = res
            self._append(i)
        while self._stack:
            lst = self._stack.pop()
            res = (self._stack[-1][-1], -1) if self._stack else (-1, -1)
            while lst:
                ret[lst.pop()] = res
        return ret


# import random


# lst = list(range(10))
# random.shuffle(lst)
# print(lst)
# a = MonotonousStack(lst)
# ret = a.find_min()
# print(ret)
