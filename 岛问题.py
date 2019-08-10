class Solution(object):
    def find_island_num(self, arr):
        ret = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 1:
                    self._infection(arr, i, j)
                    ret += 1
        return ret

    def _infection(self, arr, i, j):
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or arr[i][j] == 0 or arr[i][j] == 2:
            return
        arr[i][j] = 2
        self._infection(arr, i, j+1)
        self._infection(arr, i, j-1)
        self._infection(arr, i+1, j)
        self._infection(arr, i-1, j)


if __name__ == '__main__':
    ret = [
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]
    a = Solution()
    ans = a.find_island_num(ret)
    print(ans)
    print(ret)
