"""
数组中累积和与最小值的乘积称为指标A，给定一个数组，返回子数组中，指标A最大的值
"""


from 单调栈 import MonotonousStack
from 前缀和数组 import PrefixArray


def find_max_a(arr):
    prefix_sum_arr = PrefixArray(arr)
    monotonous = MonotonousStack(arr)
    ret = monotonous.find_min()
    ans = 0
    for index in range(len(ret)):
        l = ret[index][0]
        r = len(arr) if ret[index][1] == -1 else ret[index][1]
        ans = prefix_sum_arr.get_sum(l+1, r-1) * arr[index] if prefix_sum_arr.get_sum(l+1, r-1) * arr[index] > ans else ans
    return ans


ret = find_max_a([1, 2, 3])
print(ret)
