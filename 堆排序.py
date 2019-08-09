def build_heap(arr, end):
    """
    构造一个堆
    :param arr: arr为需要构造的堆
    :param end: end为这个堆构造到end索引为止，end索引前为一个堆结构
    :return:
    """
    for i in range(end+1):
        index = i
        heap_insert(arr, index)
        # while arr[index] > arr[abs(index-1)//2]:
        #     arr[index], arr[abs(index-1)//2] = arr[abs(index-1)//2], arr[index]
        #     index = abs(index-1)//2


def heap_insert(arr, index: int):
    """
    堆的调整，以index为堆的最后一位，向上调整堆
    :param arr: 堆的列表
    :param index: 堆最后一位的索引
    :return:
    """
    while arr[index] > arr[abs(index-1)//2]:
        arr[index], arr[abs(index - 1) // 2] = arr[abs(index - 1) // 2], arr[index]
        index = abs(index - 1) // 2


def heapify(arr: list, index, size):
    """
    假设arr已经为一个堆了，除了index位置的元素
    :param arr: 包含堆的数组
    :param index: 需要调整的位置
    :param size: 整个堆的大小
    :return:
    """
    left = index * 2 + 1
    right = index * 2 + 2
    while (left < size and arr[index] < arr[left]) or (right < size and arr[index] < arr[right]):
        if right >= size or arr[left] > arr[right]:
            arr[index], arr[left] = arr[left], arr[index]
            index = left
            left = index * 2 + 1
            right = index * 2 + 2
        else:
            arr[index], arr[right] = arr[right], arr[index]
            index = right
            left = index * 2 + 1
            right = index * 2 + 2


def heap_sort(arr):
    """
    堆排序，堆最基础的一种应用
    :param arr:
    :return:
    """
    length = len(arr)
    build_heap(arr, length-1)
    for i in range(length-1, -1, -1):
        print(arr)
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


lst = [1, 5, 4, 3, 2, 1]

heap_sort(lst)

print(lst)
