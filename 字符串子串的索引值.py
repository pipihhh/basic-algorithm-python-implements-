"""
给定一个str1和str2，判断str2是否是str1的子串，如果是，返回在str1中字符串开始位置的下标。
如果str1中不存在str2，返回-1。
"""
import random


def get_next(arr):
    if len(arr) == 1:
        return [-1, ]
    if len(arr) == 2:
        return [-1, 0]
    next_arr = [-1, 0]
    next_arr.extend((None for _ in range(2, len(arr))))
    for i in range(2, len(arr)):
        if arr[next_arr[i-1]] == arr[i-1]:
            next_arr[i] = next_arr[i-1] + 1
        else:
            tmp = next_arr[i-1] + 1
            while tmp:
                if arr[next_arr[tmp-1]] == arr[i-1]:
                    next_arr[i] = next_arr[tmp] + 1
                    break
                else:
                    tmp = next_arr[tmp-1] + 1
            else:
                next_arr[i] = 0
    return next_arr


def kmp(str1, str2, next_arr):
    i = 0
    i1 = 0
    while i < len(str1) and i1 < len(str2):
        if str1[i] == str2[i1]:
            i += 1
            i1 += 1
        elif next_arr[i1] == -1:
            i += 1
        else:
            i1 = next_arr[i1]
    return i - i1 if i1 == len(str2) else -1


def index_of(str1, str2):
    if not str1 or not str2 or len(str1) < len(str2):
        return -1
    next_arr = get_next(str2)
    return kmp(str1, str2, next_arr)


def test():
    str1 = str(random.randint(100000000000, 999999999999))
    str2 = str(random.randint(10, 99))
    ret1 = str1.find(str2)
    ret2 = index_of(str1, str2)
    if ret1 != ret2:
        return str1, str2
    return True


if __name__ == '__main__':
    for i in range(500000):
        ret = test()
        if ret != True:
            print(ret)
