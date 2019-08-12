import random, copy


class Solution(object):
    def quick_sort(self, arr):
        stack = []
        less, more = self._partition(arr, 0, len(arr) - 1)
        stack.append((more, len(arr)-1))
        stack.append((0, less))
        while stack:
            less, more = stack.pop()
            if less < more:
                l, m = self._partition(arr, less, more)
                stack.append((m, more))
                stack.append((less, l))

    def _partition(self, arr, head, tail):
        less = head - 1
        more = tail + 1
        num = arr[random.randint(head, tail)]
        cur = head
        while cur <= tail and cur < more:
            if arr[cur] < num:
                arr[cur], arr[less + 1] = arr[less + 1], arr[cur]
                less += 1
                cur += 1
            elif arr[cur] > num:
                arr[cur], arr[more - 1] = arr[more - 1], arr[cur]
                more -= 1
            else:
                cur += 1
        return less, more


a = Solution()
# a.quick_sort([1, 4, 8, 0, 9, 6, 7, 3, 2, 5])


def test():
    lst = [i for i in range(10)]
    random.shuffle(lst)
    a1 = copy.copy(lst)
    a2 = copy.copy(lst)
    a1.sort()
    a.quick_sort(a2)
    if a1 != a2:
        print(lst)
        return 1


for _ in range(50000):
    if test() == 1:
        break
