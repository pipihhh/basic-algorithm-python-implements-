import copy


class Solution(object):
    def topology_sort(self, graph):
        """
        保证此图为，无环图
        :param graph: 图
        :return:
        """
        pass

a = Solution()
ret = [
    [0, 1, float("inf"), float("inf")],
    [float("inf"), 0, float("inf"), float("inf")],
    [1, float("inf"), 0, float("inf")],
    [1, float("inf"), 1, 0]
]
ret = a.topology_sort(ret)
print(ret)
