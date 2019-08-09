import copy


class Solution(object):
    def __init__(self, arr):
        self._arr = arr
        self._x = len(arr) - 1
        self._y = len(arr[0]) - 1

    def z_print(self):
        a = [0, 0]
        b = [0, 0]
        is_up = False
        while a[1] >= b[1]:

            self._print_diag(is_up, copy.copy(a), copy.copy(b))
            if a[1] == self._y:
                a[0] += 1
            else:
                a[1] += 1
            if b[0] == self._x:
                b[1] += 1
            else:
                b[0] += 1
            is_up = not is_up

    def _print_diag(self, is_up, up, down):
        if is_up:
            self._up_print_diag(up, down)
        else:
            self._down_print_diag(up, down)

    def _up_print_diag(self, up, down):
        while up[0] <= down[0] and up[1] >= down[1]:
            print(self._arr[up[0]][up[1]])
            up[0] += 1
            up[1] -= 1

    def _down_print_diag(self, up, down):
        while down[0] >= up[0] and down[1] <= up[1]:
            print(self._arr[down[0]][down[1]])
            down[0] -= 1
            down[1] += 1


a = Solution([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
a.z_print()
