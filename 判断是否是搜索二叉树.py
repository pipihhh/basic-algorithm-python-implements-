class Response(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self, node):
        self._node = node

    def is_search_tree(self):
        ret = self._process(self._node)
        return ret.right > self._node.val

    def _process(self, node):
        if not node:
            return Response(float("-inf"), float("+inf"))
        response1 = self._process(node.left)
        response2 = self._process(node.right)
        left_max = max(response1.left, node.val)
        right_min = min(response2.right, node.val)
        return Response(left_max, right_min)
