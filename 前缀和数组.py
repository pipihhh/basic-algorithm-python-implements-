class PrefixArray(object):
    def __init__(self, arr):
        self._arr = None
        self._create_arr(arr)

    def _create_arr(self, arr):
        lst = [arr[0], ]
        for i in range(1, len(arr)):
            lst.append(lst[i-1] + arr[i])
        self._arr = lst

    def get_sum(self, i, j):
        if 0 <= i <= j < len(self._arr):
            return self._arr[j] - self._arr[i-1] if i != 0 else self._arr[j]
        raise IndexError("index out of range")


# a = PrefixArray([1, 2, 3])
# print(a.get_sum(1, 2))
