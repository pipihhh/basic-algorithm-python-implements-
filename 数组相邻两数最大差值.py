# 给定一个数组，返回排好序后的相邻两数之间的最大差值，要求时间复杂度为O(n)
import random


class FindMaxDifference(object):
    def __init__(self, arr):
        self._arr = arr

    def find_num(self):
        """
        以数组长度+1的值为长度创建一个桶列表，每个桶用一个字典来表示，字典有3个键，分别代表桶是否为空，桶内最大数，桶内最小数
        遍历列表，将列表内的值均分在桶内，列表的最小值存在0位置，列表的最大值存在最后一个桶位置
        那么答案就在，遍历每一个桶，如果这个桶有值，则它的差值为，当前桶的最大值减去上一个非空桶的最小值
        遍历每一个这样的字典，得到多个解，取最大的那一个就是答案了。
        :return: 返回这个值的答案
        """
        if not self._arr or len(self._arr) < 2:
            return 0
        length = len(self._arr)
        max_num = max(self._arr)
        min_num = min(self._arr)
        ret_list = [
            {"is_empty": True, "max": None, "min": None} for _ in range(length+1)
        ]
        for i in range(len(self._arr)):
            bucket = self._bucket(self._arr[i], max_num, min_num)
            ret_list[bucket]["is_empty"] = False
            ret_list[bucket]["max"] = ret_list[bucket]["max"] if ret_list[bucket]["max"] and self._arr[i] < ret_list[bucket]["max"] else self._arr[i]
            ret_list[bucket]["min"] = ret_list[bucket]["min"] if ret_list[bucket]["min"] and self._arr[i] > ret_list[bucket]["min"] else self._arr[i]

        ret = 0
        for d in range(1, len(ret_list)):
            if ret_list[d]["is_empty"]:
                continue
            for i in range(d-1, -1, -1):
                if not ret_list[i].get("is_empty"):
                    difference = ret_list[d]["min"] - ret_list[i]["max"]
                    ret = difference if difference > ret else ret
                    break
        return ret

    def _bucket(self, cur, max_num, min_num):
        """
        这是一个求 cur数应分在那一个桶里的简单算数函数。首先求出这组数的最大最小值，
        获取到最大最小值后，取它们的差值，除以桶的个数，算出每个桶装的数的取值范围。
        在通过将当前数与最小数做差后再与桶的取值范围相乘之后向下取整。就得到了桶的索引位置了。
        其实还有个隐性条件是，需要获得共有多少个桶。但是由于此为对象属性，所以不需要传值。
        :param cur:需要放入桶的数的值
        :param max_num:这列数的最大值
        :param min_num:这列数的最小值
        :return:桶位置的索引
        """
        return (cur - min_num) * len(self._arr) // (max_num - min_num)


lst = []
for i in range(10):
    lst.append(random.randint(0, 10))
a = FindMaxDifference(lst)
ret = a.find_num()
print(ret)
