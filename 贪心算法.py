from queue import PriorityQueue
import functools


def mini_gold2(arr):
    """
    最小铜板问题，给你一个数组，里面是每个人需要的金条长度，给你一个长度为数组内数之和的金条
    每切一次金条就要消耗当前切的金条长度的铜板
    如何使铜板的消耗最少
    :param arr:
    :return:
    """
    queue = PriorityQueue()
    for i in arr:
        queue.put(i)
    cur = 0
    _sum = 0
    while queue.qsize() > 1:
        cur = queue.get() + queue.get()
        _sum += cur
        queue.put(cur)
    return _sum


ret = mini_gold2([1, 7, 3, 6, 5, 9])
print(ret)


def cmp(a, b):
    res = a + b
    res2 = b + a
    if res < res2:
        return -1
    return 1


def lowest(arr):
    """
    最小的字典序
    :param arr:
    :return:
    """
    arr.sort(key=functools.cmp_to_key(cmp))
    return "".join(arr)


ret = lowest(["b", "a", "bcb", "**&^*&"])
print(ret)


def mini_apple(arr):
    q = PriorityQueue()
    ret = 0
    for i in arr:
        q.put(i)
    while q.qsize() > 1:
        tmp = q.get() + q.get()
        ret += tmp
        q.put(tmp)
    return ret


ret = mini_apple([1, 2, 9])
print(ret)
