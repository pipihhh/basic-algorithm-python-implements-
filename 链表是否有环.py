class Solution(object):
    def __init__(self, node, node2):
        self._node = node
        self._node2 = node2

    def _have_loop(self, node):
        slow = node
        fast = node
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = node
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def _no_loop_node(self):
        cur1 = self._node
        cur2 = self._node2
        n = 0
        while cur1.next:
            cur1 = cur1.next
            n += 1
        while cur2.next:
            cur2 = cur2.next
            n -= 1
        if cur1 != cur2:
            return None
        if n > 0:
            cur1 = self._node
            cur2 = self._node2
        else:
            cur1 = self._node2
            cur2 = self._node
        n = abs(n)
        while n:
            cur1 = cur1.next
            n -= 1
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
