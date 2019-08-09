import random, copy


def netherlands_flag(arr, start, end):
    head = start - 1
    tail = end + 1
    cur = start
    num = arr[random.randint(start, end)]
    # num = arr[start]
    while cur < tail:
        if arr[cur] == num:
            cur += 1
        elif arr[cur] < num:
            arr[cur], arr[head+1] = arr[head+1], arr[cur]
            head += 1
            cur += 1
        else:
            arr[cur], arr[tail-1] = arr[tail-1], arr[cur]
            tail -= 1
    return head+1, tail-1


def partition(arr, start, end):
    less = start - 1
    more = end
    cur = 0
    while cur <= more:
        if arr[cur] <= arr[less+1]:
            arr[cur], arr[less+1] = arr[less+1], arr[cur]
            less += 1
        cur += 1


def quick_sort(arr, start, end):
    if start < end:
        head, tail = netherlands_flag(arr, start, end)
        quick_sort(arr, start, head-1)
        quick_sort(arr, tail+1, end)


def test():
    for _ in range(500000):
        arr1 = list(range(20))
        random.shuffle(arr1)
        arr2 = copy.deepcopy(arr1)
        arr3 = copy.deepcopy(arr1)
        quick_sort(arr2, 0, 19)
        arr3.sort()
        if arr2 != arr3:
            print(arr1)
            print(arr2)
            print(arr3)
            break
    print("nice")


# test()
l = list(range(10000))
l.reverse()
quick_sort(l, 0, 9999)
print(l)
